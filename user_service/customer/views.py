from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import *
from .serializers import *

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['username']
