from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to the Jungle")

def editProfile(request):
    return HttpResponse("We are here")
# Create your views here.
