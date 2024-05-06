from django.db import models
from cart.models import Cart

class CartBook(models.Model):
    book_id = models.IntegerField()
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    price = models.IntegerField()
    total_price = models.IntegerField()
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    cart = models.ForeignKey(Cart, related_name='cart_books', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'cart_book'
