from django import forms
from .models import LoadForm

class Load(forms.ModelForm):
    class Meta:
        model = LoadForm
        fields = ['file']