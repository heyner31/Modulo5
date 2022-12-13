from .models import Service
from rest_framework import viewsets, permissions
from .serializers import ServiceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ServiceSerializer



