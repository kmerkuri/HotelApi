from rest_framework import serializers
from .models import FindHotels
class FindHotelsSerializers(serializers.ModelSerializer):
    class Meta:
        model= FindHotels
        fields = ('user','hotels')