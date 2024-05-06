from rest_framework import viewsets
from rest_framework import status
from .models import *
from .serializers import *
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

class CartBookViewSet(viewsets.ModelViewSet):
    queryset = CartBook.objects.all()
    serializer_class = CartBookSerializer

@csrf_exempt
def add_book_cart(request):
    book_id = request.POST.get('book_id')
    title = request.POST.get('title')
    image = request.POST.get('image')
    price = request.POST.get('price')
    total_price = request.POST.get('total_price')
    quantity = request.POST.get('quantity')
    cart_id = request.POST.get('cart')
    cart = Cart.objects.get(pk=cart_id)
    if CartBook.objects.filter(book_id=book_id).count() == 0:
        cart_book = CartBook.objects.create(
            book_id=book_id,
            title=title,
            image=image,
            price=price,
            total_price=total_price,
            quantity=quantity,
            cart=cart
        )
    else:
        existing_cart_book = CartBook.objects.get(book_id=book_id)
        existing_cart_book.quantity += int(quantity)
        existing_cart_book.total_price = existing_cart_book.quantity * int(price)
        existing_cart_book.save()
    return HttpResponse(status=status.HTTP_201_CREATED, content_type = 'application/json')
