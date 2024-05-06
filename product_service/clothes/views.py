from rest_framework import viewsets
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

class ClothesViewSet(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name',]

class CategoryClothesViewSet(viewsets.ModelViewSet):
    queryset = CategoryClothes.objects.all()
    serializer_class = CategoryClothesSerializer

@csrf_exempt
def get_list_clothes(request):
    resp = []
    list_clothes = Clothes.objects.all()
    for clothes in list_clothes:
        serializer = ClothesSerializer(clothes).data
        serializer['category'] = CategoryClothesSerializer(clothes.category).data
        serializer['image'] = 'http://127.0.0.1:8008' + serializer['image']
        resp.append(serializer)
    return HttpResponse(json.dumps(resp), status=status.HTTP_200_OK, content_type = 'application/json')

@csrf_exempt
def get_detail_clothes(request):
    resp = {}
    id = request.GET.get('id')
    
    if id:
        try:
            clothes = Clothes.objects.get(pk=id)
            serializer = ClothesSerializer(clothes).data
            serializer['category'] = CategoryClothesSerializer(clothes.category).data
            serializer['image'] = 'http://127.0.0.1:8008' + serializer['image']
            return HttpResponse(json.dumps(serializer), status=status.HTTP_200_OK, content_type = 'application/json')
        except:
            resp['message'] = 'Not found'
            return HttpResponse(json.dumps(resp), status=status.HTTP_404_NOT_FOUND, content_type = 'application/json')
    
    resp['message'] = 'All fields are mandatory'
    return HttpResponse(json.dumps(resp), status=status.HTTP_400_BAD_REQUEST, content_type = 'application/json')