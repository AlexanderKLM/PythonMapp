from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.views.generic import TemplateView
from social_core.pipeline.user import get_username
from .models import *
from allauth.account.auth_backends import AuthenticationBackend
from .models import Users
from django.contrib.auth.models import User

def GetUser(request, user = None):
    UserN = request.user
    if user is not None:
        UserN = get_object_or_404(User, username=user)
        print(UserN)
    context = {
        "object": UserN,
    }
    return render(request,'LogPage.html')

class UserS(TemplateView):
 template_name = 'OPCenter.html'

def get(self, request, username):
    user = get_object_or_404(User, username=username)
    print(user)
    return render(request, self.template_name, {'username': user})

# Create your views here.
