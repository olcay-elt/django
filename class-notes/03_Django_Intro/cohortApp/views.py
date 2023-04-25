from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def cohort(request):
#     return HttpResponse("Fullstack")
def cohortFS(request):
    return HttpResponse("hello FS")
def cohortAWS(request):
    return HttpResponse("<h1> Hello AWS</h1>")
