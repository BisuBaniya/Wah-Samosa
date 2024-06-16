from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, World. You are at Bisu's Home Page")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("Hello, World. You are at Bisu's About Page")

def contact(request):
    return HttpResponse("Hello, World. You are at Bisu's Contact Page")


