from django.shortcuts import render
from django.contrib.auth.models import User
from social_core.pipeline.user import get_username


def index(request):
    return render(request, 'main/mainp.html')


def GetUser(request):
    userN = get_username()
    print(userN)
    return render(request, 'main/mainp.html')


# Create your views here.
