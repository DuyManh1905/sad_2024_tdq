from rest_framework import viewsets
from rest_framework import status
from rest_framework.filters import SearchFilter
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .serializers import *
import json


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title',]

class CategoryBookViewSet(viewsets.ModelViewSet):
    queryset = CategoryBook.objects.all()
    serializer_class = CategoryBookSerializer
    
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    
@csrf_exempt
def get_list_book(request):
    resp = []
    list_books = Book.objects.all()
    for book in list_books:
        serializer = BookSerializer(book).data
        serializer['category'] = CategoryBookSerializer(book.category).data
        serializer['author'] = AuthorSerializer(book.author).data
        serializer['publisher'] = PublisherSerializer(book.publisher).data
        serializer['image'] = 'http://127.0.0.1:8008' + serializer['image']
        resp.append(serializer)
    return HttpResponse(json.dumps(resp), status=status.HTTP_200_OK, content_type = 'application/json')

@csrf_exempt
def get_detail_book(request):
    resp = {}
    id = request.GET.get('id')
    
    if id:
        try:
            book = Book.objects.get(pk=id)
            serializer = BookSerializer(book).data
            serializer['category'] = CategoryBookSerializer(book.category).data
            serializer['author'] = AuthorSerializer(book.author).data
            serializer['publisher'] = PublisherSerializer(book.publisher).data
            serializer['image'] = 'http://127.0.0.1:8008' + serializer['image']
            return HttpResponse(json.dumps(serializer), status=status.HTTP_200_OK, content_type = 'application/json')
        except:
            resp['message'] = 'Not found'
            return HttpResponse(json.dumps(resp), status=status.HTTP_404_NOT_FOUND, content_type = 'application/json')
    
    resp['message'] = 'All fields are mandatory'
    return HttpResponse(json.dumps(resp), status=status.HTTP_400_BAD_REQUEST, content_type = 'application/json')
