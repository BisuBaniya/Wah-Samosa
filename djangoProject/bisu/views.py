from django.shortcuts import render,get_object_or_404 # type: ignore
from .models import SamosaVariety

# Create your views here.
def info(req):
    samosas = SamosaVariety.objects.all()
    return render(req,'bisu/all_bisu.html',{'samosas' : samosas})

def samosa_detail(req,samosa_id):
    samosa = get_object_or_404(SamosaVariety,pk= samosa_id)
    return render(req,'bisu/samosa_detail.html',{'samosa':samosa})

