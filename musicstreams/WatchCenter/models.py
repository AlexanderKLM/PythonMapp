from django.db import models


# Create your models here.
class LinkLoad(models.Model):

    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200)
# Create your models here.
