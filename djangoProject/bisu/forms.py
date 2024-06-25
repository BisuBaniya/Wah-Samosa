from django import forms #type: ignore
from .models import SamosaVariety

class SamosaVarietyForm(forms.Form):
    samosa_variety = forms.ModelChoiceField(queryset=SamosaVariety.objects.all(),label="Select Samosa Variety")
    
