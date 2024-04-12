from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_djnago(request):
    return HttpResponse('<h1>Hello Django</h1>, <p>this is zeeshan khan </p>')

def learn_python(request):
    return HttpResponse("<h3>learn python</h3>")



