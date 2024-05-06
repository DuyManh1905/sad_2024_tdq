from django.db import models
from user.models import NguoiDung

class Customer(NguoiDung):
    delivery_address = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'customser'
        app_label = 'customer'
