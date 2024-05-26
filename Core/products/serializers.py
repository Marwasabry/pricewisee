# serializers.py

from rest_framework import serializers
from .models import Brand, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name','brand', 'price','description','url','image_url']

'''class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']
        '''
from rest_framework import serializers

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()
from rest_framework import serializers
from .models import Brand, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'price', 'description', 'url', 'image_url']

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()
