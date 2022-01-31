from dataclasses import fields
from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "get_absolute_url",
            "price",
            "get_image",
            "get_thumbnail"
        )
