from rest_framework import viewsets
from rest_framework import status
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .models import Shipment
from .serializers import ShipmentSerializer

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    
@csrf_exempt
def update_shipment(request):
    shipment_status = Shipment(
        name = request.POST.get('username'),
        mobile = request.POST.get('mobile'),
        delivery_address = request.POST.get('delivery_address'),
        order_id = request.POST.get('order_id'),
        shipment_status = request.POST.get('shipment_status'),
        payment_status = request.POST.get('payment_status'),
    )
    shipment_status.save()
    message = {'message': 'Update sucessfully!'}
    return HttpResponse(json.dumps(message), status=status.HTTP_200_OK, content_type = 'application/json')

@csrf_exempt
def shipment_status(request):
    resp = {}
    order_id = request.GET.get('order_id')
    resp['shipment_status'] = ShipmentSerializer(Shipment.objects.filter(order_id=order_id), many=True).data
    return HttpResponse(json.dumps(resp), status=status.HTTP_200_OK, content_type = 'application/json')
    
    
    