from rest_framework import serializers
from .models import *

class NguoiDungSerializer(serializers.ModelSerializer):
    class Meta:
        model = NguoiDung
        fields = ['id', 'username', 'password', 'name', 'address', 'mobile', 'role',]