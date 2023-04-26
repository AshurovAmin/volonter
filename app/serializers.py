from rest_framework import serializers

from .models import Category, Position


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'