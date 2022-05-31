
from django.urls import path, include
from .views import UploadFile


urlpatterns = [
    path('', UploadFile, name='OPC'),

]
