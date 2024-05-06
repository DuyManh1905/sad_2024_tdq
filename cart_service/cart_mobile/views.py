from rest_framework import viewsets
from rest_framework import status
from .models import *
from .serializers import *
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

class CartMobileViewSet(viewsets.ModelViewSet):
    queryset = CartMobile.objects.all()
    serializer_class = CartMobileSerializer
    
@csrf_exempt
def add_mobile_cart(request):
    mobile_id = request.POST.get('mobile_id')
    name = request.POST.get('name')
    image = request.POST.get('image')
    price = request.POST.get('price')
    total_price = request.POST.get('total_price')
    quantity = request.POST.get('quantity')
    cart_id = request.POST.get('cart')
    cart = Cart.objects.get(pk=cart_id)
    if CartMobile.objects.filter(mobile_id=mobile_id).count() == 0:
        cart_mobile = CartMobile.objects.create(
            mobile_id=mobile_id,
            name=name,
            image=image,
            price=price,
            total_price=total_price,
            quantity=quantity,
            cart=cart
        )
    else:
        existing_cart_mobile = CartMobile.objects.get(mobile_id=mobile_id)
        existing_cart_mobile.quantity += int(quantity)
        existing_cart_mobile.total_price = existing_cart_mobile.quantity * int(price)
        existing_cart_mobile.save()
    return HttpResponse(status=status.HTTP_201_CREATED, content_type = 'application/json')