from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from social_core.pipeline.user import get_username
from .models import *
from allauth.account.auth_backends import AuthenticationBackend
from .models import Users
from django.contrib.auth.models import User

def GetUser(request, user=None):
    UserN = None
    if user is not None:
        UserN = User.get_username()
        print(UserN)
    context = {
        "object": UserN,
    }
    return redirect('http://127.0.0.1:8000/OPCenter/<str:username>/', { user: UserN})


# Create your views here.
