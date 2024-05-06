from rest_framework import serializers
from .models import *

class CategoryMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMobile
        fields = '__all__'

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__' 
