from django.db import models
from cart.models import Cart

class CartMobile(models.Model):
    mobile_id = models.IntegerField()
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total_price = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    cart = models.ForeignKey(Cart, related_name='cart_mobiles', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'cart_mobiles'