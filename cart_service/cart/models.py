from django.db import models

class Cart(models.Model):
    customer_id = models.IntegerField()
    
    class Meta:
        db_table = 'cart'
