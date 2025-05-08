from django.shortcuts import render
from django.http import HttpResponse
from home.singleton import get_global_object

# Create your views here.


def credits(request):
    global_obj = get_global_object()
    content1 = global_obj.data + "\n\n"
    content2 = "Micky, the creator of this project, is a software engineer with a passion for web development and open-source contributions. He has a strong background in Python and Django, and he enjoys building scalable and efficient applications. Micky is also an advocate for clean code and best practices in software development."
    # import IPython; IPython.embed()
    return HttpResponse(content1 + content2, content_type="text/plain")

def news(request):
    data = {
        "news": [
            "RifMates now has a news page!",
            "RifMates is now open source!",
        ],
    }
    return render(request, "news2.html", data)