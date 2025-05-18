from django.shortcuts import render
from django.http import HttpResponse
from fs_viewer.singleton import get_global_object

from .forms import StatementForm
# Create your views here.


def credits(request):
    content = "Micky, the creator of this project, is a software engineer with a passion for web development and open-source contributions. He has a strong background in Python and Django, and he enjoys building scalable and efficient applications. Micky is also an advocate for clean code and best practices in software development."
    # import IPython; IPython.embed()
    return HttpResponse(content, content_type="text/plain")

def news(request):
    data = {
        "news": [
            "RifMates now has a news page!",
            "RifMates is now open source!",
        ],
    }
    return render(request, "news2.html", data)

def company_report_select(request):
    # Instantiate the Query object
    global_obj = get_global_object()
    query = global_obj.query

    # Get the company CIKs
    company_cik = query.company_cik

    # Render the selection template with the company CIKs
    return render(request, "company_report_select.html", {"company_cik": company_cik})


def statement_view(request):
    # Instantiate the Query object
    # In a real application, you might want to manage the lifecycle of this
    # object more carefully (e.g., single instance, caching).
    global_obj = get_global_object()
    query = global_obj.query

    # Populate company choices from the query object
    company_choices = [(cik, name) for name, cik in query.company_cik.items()]
    # Or simply use names if you prefer, mapping back to CIK later
    # company_choices = [(name, name) for name in query.companies]

    form = StatementForm(request.POST or None) # Handle GET (None) and POST data
    # Update the choices for the company field
    form.fields['company'].choices = company_choices

    statement_data = None
    selected_company_name = None
    selected_statement_type = None
    error_message = None

    if request.method == 'POST' and form.is_valid():
        selected_cik = int(form.cleaned_data['company']) # Get CIK directly
        # If using names, get name: selected_company_name = form.cleaned_data['company']
        # Then map name to CIK: selected_cik = query.company_cik.get(selected_company_name)

        selected_statement_type = form.cleaned_data['statement_type']

        # Get the company name for display purposes
        selected_company_name = next(
            (name for name, cik in query.company_cik.items() if cik == selected_cik),
            str(selected_cik) # Fallback if CIK not found in initial list (shouldn't happen with our choices)
        )

        # 1. Get all filings for the CIK, sorted by date (cik_adsh does this)
        filings = query.cik_adsh(selected_cik)

        if not filings:
            error_message = f"No filings found for {selected_company_name} (CIK: {selected_cik})."
        else:
            # 2. Find the latest filing. cik_adsh returns sorted list, so last is latest.
            #    We might want to filter by report type (e.g., 10-K for FY, 10-Q for Q)
            #    For simplicity here, we just take the very last filing.
            latest_filing = filings[-1]
            latest_adsh = latest_filing['adsh']
            latest_filing_date = latest_filing['filed']

            # 3. Get the statement data for the latest ADSH and selected statement type
            all_statement_lines = query.adsh_stmt(latest_adsh, selected_statement_type)

            # 4. Filter for lines that have 'ddate' and 'value'
            statement_data = [
                item for item in all_statement_lines
                if 'ddate' in item and 'value' in item
            ]

            if not statement_data:
                 error_message = f"No {selected_statement_type} data found in the latest filing ({latest_adsh}, filed {latest_filing_date.date()}) for {selected_company_name}."
                 # As a fallback/example, try the hardcoded example ADSH if the primary failed
                 # REMOVE this fallback in a real app, it's just for demonstrating with mock data
                 if selected_statement_type == 'IS' and selected_company_name == "Microsoft Corp.":
                      print("Trying hardcoded example ADSH for IS...")
                      statement_data = [
                            item for item in query.adsh_stmt('0000950170-23-014423', 'IS')
                            if 'ddate' in item and 'value' in item
                      ]
                      if statement_data:
                           error_message = f"Could not find {selected_statement_type} data in the latest filing ({latest_adsh}). Displaying example data from '0000950170-23-014423' instead."
                      else:
                           error_message = f"No {selected_statement_type} data found in the latest filing ({latest_adsh}, filed {latest_filing_date.date()}) or example data for {selected_company_name}."


    context = {
        'form': form,
        'statement_data': statement_data,
        'selected_company': selected_company_name,
        'selected_statement_type': selected_statement_type,
        'error_message': error_message,
    }

    return render(request, 'statement_view.html', context)