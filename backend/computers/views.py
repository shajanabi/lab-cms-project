from django.shortcuts import render

from rest_framework import filters, viewsets

from .models import Computer
from .serializers import ComputerSerializer


class ComputerViewSet(viewsets.ModelViewSet):
	queryset = Computer.objects.all()
	serializer_class = ComputerSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['pc_name', 'ip_address', 'status']

# Create your views here.
