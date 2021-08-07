from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    courses = [
        { 'title': 'Django'},
        { 'title': 'Python'},
        {'title': 'Data science'},
    ]
    return render(request, 'demo/welcome.html', {
        'show': True,
        'courses' : courses
    })
    #return HttpResponse("hello world")

def hello_string(request):
     return "hello world"
