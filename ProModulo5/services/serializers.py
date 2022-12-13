from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('title', 'subtitle', 'content', 'image', 'pricing', 'created', 'updated')
        read_only_fields = ('created', 'updated', )