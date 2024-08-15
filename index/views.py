from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def display_index(request):
    return HttpResponse("Hello World!")
