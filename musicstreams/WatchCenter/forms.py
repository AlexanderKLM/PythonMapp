from django import forms
from .models import LinkLoad

class LinkForm(forms.ModelForm):
    class Meta:
        model = LinkLoad
        fields = ['line1', 'line2']