from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>this is Home page of first Application (course)</h1>") 

def learn_python(request):
    return HttpResponse("<h3>learn python</h3>")

def learn_django(request):
    return HttpResponse("<h3>learn django</h3>")

def learn_javascript(request):
    return HttpResponse("<h3>learn javascript</h3>")

def learn_react(request):
    return HttpResponse("<h3>learn react</h3>")
