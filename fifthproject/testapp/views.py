from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def f_view(request):
    return HttpResponse('<h1> First View</h1>')

def s_view(request):
    return HttpResponse('<h1> Second View</h1>')

def t_view(request):
    return HttpResponse('<h1> Third View</h1>')

def fo_view(request):
    return HttpResponse('<h1> Fouth View</h1>')

def fi_view(request):
    return HttpResponse('<h1> Fifth View</h1>')