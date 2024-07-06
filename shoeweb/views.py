from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("hello")

def shoeweb(request):
    return render(request,"index.html")