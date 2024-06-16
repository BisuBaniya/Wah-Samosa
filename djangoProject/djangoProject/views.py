from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World. You are at Bisu's Home Page")

def about(request):
    return HttpResponse("Hello, World. You are at Bisu's About Page")

def contact(request):
    return HttpResponse("Hello, World. You are at Bisu's Contact Page")


