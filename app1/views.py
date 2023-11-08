from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mike(request):
    return HttpResponse('hii mike how are you')
