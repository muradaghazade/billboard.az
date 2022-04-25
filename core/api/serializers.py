from dataclasses import field
from rest_framework import serializers
from core.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'support_price', 'code', 'size', 'image', 'category')