# files/serializers.py
from rest_framework import serializers
from .models import CSV

class CSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSV
        fields = ['id', 'name', 'file', 'uploaded_at']
