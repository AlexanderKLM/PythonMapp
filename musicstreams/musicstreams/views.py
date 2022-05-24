from django.shortcuts import render


def GetUser(request, username=None):
    user_obj = request.user.get_username(username)
    context = {
        "object": user_obj
    }
    return render(request, "OPCenter.html/Name.html", context={})
