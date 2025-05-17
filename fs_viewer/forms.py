# sec_viewer/forms.py
from django import forms

class StatementForm(forms.Form):
    # Choices will be populated dynamically in the view
    company = forms.ChoiceField(label="Select Company")

    statement_type = forms.ChoiceField(
        label="Select Statement Type",
        choices=[
            ('IS', 'Income Statement'),
            ('BS', 'Balance Sheet'),
            ('CF', 'Cash Flow'),
        ]
    )