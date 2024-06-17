from django.shortcuts import render

# Create your views here.
def info(req):
    return render(req,'bisu/all_bisu.html')

def order(req):
    return render(req,'bisu/all_bisu.html')

