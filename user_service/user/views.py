from rest_framework import viewsets, status
from rest_framework import status
from django.contrib.auth.models import User
from .models import *
from customer.models import *
from .serializers import *
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

class NguoiDungViewSet(viewsets.ModelViewSet):
    queryset = NguoiDung.objects.all()
    serializer_class = NguoiDungSerializer
    

@csrf_exempt
def check_user(request):
    mobile = request.POST.get('mobile')
    password = request.POST.get('password')
    
    if mobile and password:
        user = NguoiDung.objects.filter(mobile=mobile, password=password).first()
        if user:
            user = NguoiDungSerializer(user).data
            customer = Customer.objects.filter(mobile=mobile, password=password).first()
            if customer:
                user['delivery_address'] = customer.delivery_address
            return HttpResponse(json.dumps(user), status=status.HTTP_200_OK, content_type = 'application/json')
        else: 
            message = {'message': 'Wrong username or password!'}
            return HttpResponse(json.dumps(message), status=status.HTTP_404_NOT_FOUND, content_type = 'application/json')
    message = {'message': 'Mobile and password are required!'}
    return HttpResponse(json.dumps(message), status=status.HTTP_400_BAD_REQUEST, content_type = 'application/json')
        
    