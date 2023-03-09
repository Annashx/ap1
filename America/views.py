from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'inicio.html')

def Brasil(request):
    return render(request,'brasil.html')

def Argentina(request):
    return render(request, 'argentina.html')


def Bolivia(request):
    return render(request, 'bolivia.html')
