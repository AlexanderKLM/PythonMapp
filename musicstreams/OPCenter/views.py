from django.shortcuts import render
from django.views.generic import TemplateView


from django.shortcuts import render, HttpResponse
from .forms import Load

def UploadFile(request):
    if request.method == 'POST':
        form = Load(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'OPCenter.html', {'form': form})
    else:
        form = Load()
        context = {
            'form':form,
        }
    return render(request, 'OPCenter.html', context)


