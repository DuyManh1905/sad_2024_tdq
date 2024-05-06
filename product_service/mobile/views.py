from rest_framework import viewsets
from rest_framework import status
from rest_framework.filters import SearchFilter
from .models import *
from .serializers import *
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

class MobileViewSet(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name',]

class CategoryMobileViewSet(viewsets.ModelViewSet):
    queryset = CategoryMobile.objects.all()
    serializer_class = CategoryMobileSerializer

@csrf_exempt
def get_list_mobile(request):
    resp = []
    list_mobiles = Mobile.objects.all()
    for mobile in list_mobiles:
        serializer = MobileSerializer(mobile).data
        serializer['category'] = CategoryMobileSerializer(mobile.category).data
        serializer['image'] = 'http://127.0.0.1:8008/' + serializer['image']
        resp.append(serializer)
    return HttpResponse(json.dumps(resp), status=status.HTTP_200_OK, content_type = 'application/json')

@csrf_exempt
def get_detail_mobile(request):
    resp = {}
    id = request.GET.get('id')
    
    if id:
        try:
            mobile = Mobile.objects.get(pk=id)
            serializer = MobileSerializer(mobile).data
            serializer['category'] = CategoryMobileSerializer(mobile.category).data
            serializer['image'] = 'http://127.0.0.1:8008/' + serializer['image']
            return HttpResponse(json.dumps(serializer), status=status.HTTP_200_OK, content_type = 'application/json')
        except:
            resp['message'] = 'Not found'
            return HttpResponse(json.dumps(resp), status=status.HTTP_404_NOT_FOUND, content_type = 'application/json')
    
    resp['message'] = 'All fields are mandatory'
    return HttpResponse(json.dumps(resp), status=status.HTTP_400_BAD_REQUEST, content_type = 'application/json')