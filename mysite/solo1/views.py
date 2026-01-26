from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Letting go isn't the end of the world; it's the beginning of a new life.")