from rest_framework import serializers
from .models import Phone

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ["id", "name", "subcategory", "price", "stock", "description", "published_date", "screen_size", "ram", "rom", "battery_capacity", "camera_resolution"]