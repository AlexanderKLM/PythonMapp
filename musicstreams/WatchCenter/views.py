from django.shortcuts import render
from .forms import LinkForm
from .models import LinkLoad


def UploadLink(request):
    if request.method == 'POST':
        form = LinkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'getmusic.html', {'form': form})
    else:
        form = LinkForm()
        context = {
            'form': form,
        }
    return render(request, 'getmusic.html', context)

# Create your views here.
