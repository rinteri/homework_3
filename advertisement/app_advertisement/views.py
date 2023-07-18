from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Подписывайтесь на tori_ravioli</h1>')

def ind(request):
    return HttpResponse('<h1>Hello world</h1>')

