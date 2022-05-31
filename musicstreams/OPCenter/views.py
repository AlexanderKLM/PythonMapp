
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import TemplateView
from social_core.pipeline.user import get_username

from .forms import Load
from .models import LoadForm




def UploadFile(request, username):
    if request.method == 'POST':
        form = Load(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'OPCenter.html' ,{'form': form})
    else:
        form = Load()
        context = {
            'form':form,
        }

    return render(request,  'OPCenter.html' ,context)


