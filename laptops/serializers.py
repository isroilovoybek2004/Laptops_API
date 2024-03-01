from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from laptops.models import Laptops, Manufacturer, LaptopReview


class LaptopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptops
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class LaptopReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptopReview
        fields = '__all__'