from django.db import models

class ClientData(models.Model):
    phone = models.CharField(max_length=11, blank=False, default='')
    fullname = models.CharField(max_length=50,blank=False, default='')
    address = models.CharField(max_length=50,blank=False, default='')
    email = models.CharField(max_length=30,blank=False, default='')
    verified = models.BooleanField(default=False)

class OrderData(models.Model):
    GALLON_1 = 1
    GALLON_2 = 2
    HALF_GALLON = 3
    _500ML = 4
    _350ML = 5

    ITEM_TYPES = {
        (GALLON_1, '1 Gallon (with faucet)'),
        (GALLON_2, '1 Gallon (for despenser)'),
        (HALF_GALLON, 'Half gallon'),
        (_500ML, '500ml bottled water'),
        (_350ML, '350ml bottled water'),
    }

    phone = models.CharField(max_length=11, blank=False, default='')
    fullname = models.CharField(max_length=50,blank=False, default='')
    address = models.CharField(max_length=50,blank=False, default='')
    item = models.PositiveSmallIntegerField(choices=ITEM_TYPES, default=1)
    pendingPayment = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    Paid = models.BooleanField(default=False)
    Delivered = models.BooleanField(default=False)
    reservationDate = models.DateTimeField()
