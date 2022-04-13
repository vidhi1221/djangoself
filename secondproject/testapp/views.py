from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gm(request):
    return HttpResponse('<h1> Good Morning </h1>')

def ga(request):
    return HttpResponse('<h1> Good Afternoon </h1>')

def ge(request):
    return HttpResponse('<h1> Good Evening </h1>')

