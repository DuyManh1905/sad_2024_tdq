from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'password', 'name', 'address', 'mobile', 'role', 'delivery_address',]