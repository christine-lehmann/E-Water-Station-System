from django.db import models

class ClientData(models.Model):
    phone = models.CharField(max_length=70, blank=False, default='')
    fullname = models.CharField(max_length=200,blank=False, default='')
    address = models.CharField(max_length=200,blank=False, default='')
    email = models.CharField(max_length=200,blank=False, default='')
    reservation = models.DateField()
    ##item = models.CharField(max_length=200,blank=False, default='')