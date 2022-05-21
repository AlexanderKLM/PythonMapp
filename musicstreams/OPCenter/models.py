from django.db import models

# Create your models here.
class LoadForm(models.Model):

    file = models.FileField(upload_to='documents/')
# Create your models here.
