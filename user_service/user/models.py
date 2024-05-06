from django.db import models

class NguoiDung(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=12)
    role = models.CharField(max_length=20)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'nguoidung'
        app_label = 'user'
        

