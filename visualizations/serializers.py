from rest_framework import serializers
from .models import Visualization

class VisualizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visualization
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
