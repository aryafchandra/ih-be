from rest_framework import serializers
from .models import Dashboard

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'user']

    def validate_csv(self, value):
        if not value:
            raise serializers.ValidationError("CSV file must be provided.")
        return value
