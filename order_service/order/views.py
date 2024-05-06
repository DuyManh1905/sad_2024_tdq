from rest_framework import viewsets
from rest_framework import status
from django.http import HttpResponse
import json
import httpx
import asyncio
from django.views.decorators.csrf import csrf_exempt

from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
@csrf_exempt
def add_order(request):
    username = request.POST.get('username')
    customer_id = request.POST.get('customer_id')
    mobile = request.POST.get('mobile')
    delivery_address = request.POST.get('delivery_address')
    total_price = request.POST.get('total_price')
    data = {'customer_id': customer_id}
    async def get_response():
        async with httpx.AsyncClient() as client:
            cart = await client.get('http://127.0.0.1:8002/cart-detail/', params=data)
            cart_delete = await client.post('http://127.0.0.1:8002/delete/', data=data)
            return cart.json()
    cart = asyncio.run(get_response())
    order_product = []
    order_product.extend(cart['cart_book'])
    order_product.extend(cart['cart_clothes'])
    order_product.extend(cart['cart_mobile'])
    data = {
        'username': username,
        'mobile': mobile,
        'delivery_address': delivery_address,
        'order_product': json.dumps(order_product),
        'total_price': total_price,
        'customer_id': customer_id,
    }
    order_task = httpx.post('http://localhost:8003/order/', data=data)
    print(order_task.status_code)
    if order_task.status_code == 201:
        return HttpResponse(json.dumps({'message': 'Success to add order!'}), status=status.HTTP_201_CREATED, content_type = 'application/json')
    return HttpResponse(json.dumps({'message': 'Something went wrong!'}), status=status.HTTP_204_NO_CONTENT, content_type = 'application/json')
    
@csrf_exempt
def get_list_order(request):
    customer_id = request.GET.get('customer_id')
    list_orders = Order.objects.filter(customer_id=customer_id)
    print(list_orders)
    serializer = OrderSerializer(list_orders, many=True).data
    return HttpResponse(json.dumps(serializer), status=status.HTTP_200_OK, content_type = 'application/json')

@csrf_exempt
def detail_order(request):
    order_id = request.GET.get('order_id')
    try:
        order = Order.objects.get(pk=order_id)
        serializer = OrderSerializer(order).data
        return HttpResponse(json.dumps(serializer), status=status.HTTP_200_OK, content_type = 'application/json')
    except:
        return HttpResponse(json.dumps({'message': 'Not found'}), status=status.HTTP_404_NOT_FOUND, content_type = 'application/json')
    
    