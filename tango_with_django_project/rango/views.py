from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Rango says hello partner!<br><a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("This is an about page.<br><a href='/rango/'>Index</a>")