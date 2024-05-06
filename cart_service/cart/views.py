from rest_framework import viewsets
from rest_framework import status
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .models import Cart
from cart_book.models import CartBook
from cart_clothes.models import CartClothes
from cart_mobile.models import CartMobile
from .serializers import *
from cart_book.serializers import CartBookSerializer
from cart_clothes.serializers import CartClothesSerializer
from cart_mobile.serializers import CartMobileSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

@csrf_exempt
def get_id_cart(request):
    customer_id = request.GET.get('customer_id')
    cart_id = Cart.objects.filter(customer_id=customer_id).first().id
    data = {'cart_id': cart_id}
    return HttpResponse(json.dumps(data), status=status.HTTP_200_OK, content_type = 'application/json')
    
@csrf_exempt
def get_cart(request):
    resp = {}
    customer_id = request.GET.get('customer_id')
    
    if customer_id:
        try:
            cart = Cart.objects.get(pk=customer_id)
            resp['message'] = 'Success'
            resp['cart_book'] = CartBookSerializer(CartBook.objects.filter(cart=cart.id), many=True).data
            resp['cart_clothes'] = CartClothesSerializer(CartClothes.objects.filter(cart=cart.id), many=True).data
            resp['cart_mobile'] = CartMobileSerializer(CartMobile.objects.filter(cart=cart.id), many=True).data
            return HttpResponse(json.dumps(resp), status=status.HTTP_200_OK, content_type = 'application/json')
        except:
            resp['message'] = 'Not found'
            return HttpResponse(json.dumps(resp), status=status.HTTP_404_NOT_FOUND, content_type = 'application/json')
    resp['message'] = 'customer_id required!'
    return HttpResponse(json.dumps(resp), status=status.HTTP_400_BAD_REQUEST, content_type = 'application/json')

@csrf_exempt
def delete_cart(request):
    resp = {}
    customer_id = request.POST.get('customer_id')
    try:
        cart = Cart.objects.filter(customer_id=customer_id).first()
        CartBook.objects.filter(cart=cart.id).delete()
        CartClothes.objects.filter(cart=cart.id).delete()
        CartMobile.objects.filter(cart=cart.id).delete()
        resp['message'] = 'Deleted successfully!'
        return HttpResponse(json.dumps(resp), status=status.HTTP_200_OK, content_type = 'application/json')
    except:
        resp['message'] = 'Failed to delete. Something went wrong!'
        return HttpResponse(json.dumps(resp), status=status.HTTP_204_NO_CONTENT, content_type = 'application/json')