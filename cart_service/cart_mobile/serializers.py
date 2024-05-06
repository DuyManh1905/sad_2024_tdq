from rest_framework import serializers
from .models import CartMobile

class CartMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartMobile
        fields = '__all__'