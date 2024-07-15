from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore

def home(request):
    # return HttpResponse("Hello, World. You are at Bisu's Home Page")
    context = {
        'path':request.path,
        'method':request.method,
        'headers':dict(request.headers),
    }
    return render(request,'website/index.html',context)

def about(request):
    return HttpResponse("Hello, World. You are at Bisu's About Page")

def contact(request):
    # return HttpResponse("Hello, World. You are at Bisu's Contact Page")
    htmlContent = "<h1><i>Hello, World. You are at Bisu's Contact Page</i></h1>"
    return HttpResponse(htmlContent)


