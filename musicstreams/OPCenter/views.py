from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from django.shortcuts import render, HttpResponse
from social_core.pipeline.user import get_username
from .forms import Load
from .models import LoadForm

from social_core.pipeline.user import get_username



def UploadFile(request):

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
        USern= request.user.get_username()
        user_f = request.user.last_name()
        print(USern, user_f)
    return render(request,  'OPCenter.html' ,context, USern)





def GetUser(request, username=None):
    user_obj = request.user.get_username()
    user_f = request.user.last_name()
    context = {
        "object": user_obj
    }
    print (user_f,user_obj)
    return render(request, "OPCenter.html/Name.html", context={})



