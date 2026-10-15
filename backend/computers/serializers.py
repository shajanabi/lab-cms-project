from rest_framework import serializers

from .models import Computer


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ['id', 'pc_name', 'ip_address', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']