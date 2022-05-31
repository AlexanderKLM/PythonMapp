from django.db import models
from django.urls import reverse

class Users(models.Model):
    Username = models.CharField('Username', max_length=150)
    Firstname = models.CharField('First name', max_length=150)
    Lastname = models.CharField('Last name', max_length=150)
    Emailaddress = models.CharField('', max_length=150)

def get_absolute_url(username):
    return reverse('post', kwargs={'user_name': username.slug})
# Create your models here.
