
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse

from .forms import Load
from .models import LoadForm




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

    return render(request,  'OPCenter.html' ,context)





def GetUser(request, user=None):
    UserN = None
    if user is not None:
        UserN = User.get_username()
        print(UserN)
    context = {
        "object": UserN,
    }
    return render(request, "Name.html", context=context)

def user_page(response, username):
    username = str(User.objects.get(username=response.user.username))
    userphoto = username[0:2]
    return render(response, "OPCenter.html", {"userphoto": userphoto})


