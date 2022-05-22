from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from django.shortcuts import render, HttpResponse
from social_core.pipeline.user import get_username
from .forms import Load
from .models import LoadForm


def UploadFile(request):
    form_class=LoadForm
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





def GetUser(request):
    userN = get_username()
    print(userN)
    return render(request, 'OPCenter.html')



