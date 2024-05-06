from rest_framework import serializers
from .models import CartClothes

class CartClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartClothes
        fields = '__all__'