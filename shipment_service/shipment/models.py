from django.db import models

class Shipment(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    delivery_address = models.CharField(max_length=255)
    order_id = models.IntegerField()
    shipment_status = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'shipment'
