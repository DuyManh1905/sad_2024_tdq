from rest_framework import serializers
from .models import CartBook

class CartBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartBook
        fields = '__all__'