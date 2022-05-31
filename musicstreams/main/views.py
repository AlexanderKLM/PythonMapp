from django.shortcuts import render


def index(request):
    return render(request, 'main/mainp.html')

# Create your views here.
