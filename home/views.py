from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def credits(request):
    content = "Micky, the creator of this project, is a software engineer with a passion for web development and open-source contributions. He has a strong background in Python and Django, and he enjoys building scalable and efficient applications. Micky is also an advocate for clean code and best practices in software development."
    return HttpResponse(content, content_type="text/plain")