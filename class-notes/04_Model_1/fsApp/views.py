from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse ("welcome FS cohort path fs")
def home2(request):
    return HttpResponse ("welcome FS2 cohort path fshome")