from django.shortcuts import render
from django.http import HttpResponse
#from basic.modules import pytz_demo

def hello(request):
    courses = [
        { 'title': 'Django'},
        { 'title': 'Python'},
        {'title': 'Data science'},
    ]
    return render(request, 'demo/welcome.html', {
        'show': True,
        'courses' : courses
        #'all_timezone': pytz_demo.findAlltz()
    })
    #return HttpResponse("hello world")

def hello_string(request):
     return "hello world"
