from django.db import models

class Order(models.Model):
    username = models.CharField(max_length=255)
    mobile = models.CharField(max_length=12)
    delivery_address = models.CharField(max_length=255)
    order_product = models.JSONField()
    total_price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    isDone = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    customer_id = models.IntegerField()
    
    class Meta:
        db_table = 'order'
        ordering = ['-date']
