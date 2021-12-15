from rest_framework import serializers
from restaurantes.models import Restaurants

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = "__all__"
        #exclude = ['name',]