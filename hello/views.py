from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, Azure Ninjas. Keep Rocking")
