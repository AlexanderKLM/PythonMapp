from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def user_page(response, username):
    username = str(User.objects.get(username=response.user.username))
    userphoto = username[0:2]
    return render(response, "Name.html", {"userphoto": userphoto})

