from rest_framework import viewsets
from rest_framework import status
from .models import *
from .serializers import *
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

class CartClothesViewSet(viewsets.ModelViewSet):
    queryset = CartClothes.objects.all()
    serializer_class = CartClothesSerializer
    
@csrf_exempt
def add_clothes_cart(request):
    clothes_id = request.POST.get('clothes_id')
    name = request.POST.get('name')
    image = request.POST.get('image')
    price = request.POST.get('price')
    total_price = request.POST.get('total_price')
    quantity = request.POST.get('quantity')
    cart_id = request.POST.get('cart')
    cart = Cart.objects.get(pk=cart_id)
    if CartClothes.objects.filter(clothes_id=clothes_id).count() == 0:
        cart_clothes = CartClothes.objects.create(
            clothes_id=clothes_id,
            name=name,
            image=image,
            price=price,
            total_price=total_price,
            quantity=quantity,
            cart=cart
        )
    else:
        existing_cart_clothes = CartClothes.objects.get(clothes_id=clothes_id)
        existing_cart_clothes.quantity += int(quantity)
        existing_cart_clothes.total_price = existing_cart_clothes.quantity * int(price)
        existing_cart_clothes.save()
    return HttpResponse(status=status.HTTP_201_CREATED, content_type = 'application/json')