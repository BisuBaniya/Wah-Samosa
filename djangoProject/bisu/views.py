from django.shortcuts import render,get_object_or_404 # type: ignore
from .models import SamosaVariety, Store
from .forms import SamosaVarietyForm

# Create your views here.
def info(req):
    samosas = SamosaVariety.objects.all()
    return render(req,'bisu/all_bisu.html',{'samosas' : samosas})

def samosa_detail(req,samosa_id):
    samosa = get_object_or_404(SamosaVariety,pk= samosa_id)
    return render(req,'bisu/samosa_detail.html',{'samosa':samosa})

def samosa_view_store(req):
    stores = None
    if req.method == 'POST':
        form = SamosaVarietyForm(req.POST)
        if form.is_valid():
            samosa_variety = form.cleaned_data['samosa_variety']
            stores = Store.objects.filter(samosa_varieties = samosa_variety)
    else:
        form = SamosaVarietyForm()    
    return render(req,'bisu/samosa_stores.html',{"stores":stores,'form':form})

