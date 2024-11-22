from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sports(request):
    return HttpResponse('hello everyone, wellcome to Django world!!')
