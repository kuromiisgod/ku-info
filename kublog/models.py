from django.db import models
from kublog import consts

class PostOne(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)
    content = models.CharField(max_length=2200)
    place = models.CharField(choices=consts.PREFECTURES,max_length=30)
    created_by = models.CharField(max_length=30)

class Contact(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField()
    contact_message = models.CharField(max_length=2200)





