from django.db import models

class ClientData(models.Model):
    phone = models.CharField(max_length=11, blank=False, default='')
    fullname = models.CharField(max_length=50,blank=False, default='')
    address = models.CharField(max_length=50,blank=False, default='')
    email = models.CharField(max_length=30,blank=False, default='')

class OrderData(models.Model):
    item_id = models.PositiveIntegerField(blank=True, null=True)
    phone = models.CharField(max_length=11, blank=False, default='')
    fullname = models.CharField(max_length=50,blank=False, default='')
    address = models.CharField(max_length=50,blank=False, default='')
    email = models.CharField(max_length=30,blank=False, default='')
    item = models.CharField(max_length=31,blank=False, default='GALLON 1')
    quantity = models.IntegerField(blank=True, null=True)
    payment = models.IntegerField(blank=True, null=True)
    reservationDate = models.DateTimeField()

class OrderStatus(models.Model):
    item_id = models.PositiveIntegerField(blank=True, null=True)
    phone = models.CharField(max_length=11, blank=False, default='')
    fullname = models.CharField(max_length=50,blank=False, default='')
    address = models.CharField(max_length=50,blank=False, default='')
    email = models.CharField(max_length=30,blank=False, default='')
    item = models.CharField(max_length=30,blank=False, default='GALLON 1')
    quantity = models.IntegerField(blank=True, null=True)
    payment = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=15,blank=False, default='Preparing')
    DateAccepted = models.DateTimeField(auto_now_add=True)

class Order_stats_sales(models.Model):
    item_id = models.PositiveIntegerField(blank=True, null=True)
    item = models.CharField(max_length=30,blank=False, default='GALLON 1')
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
