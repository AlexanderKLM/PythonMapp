from . import views
from django.urls import path

urlpatterns = [
   path('', views.UploadLink, name='Добавление песен')
]