from rest_framework import serializers

from .models import (
    CustomUser, Organization, Dashboard,
    CSVFile, Visualization
)


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'role', 'is_active', 'organization']


class CSVFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVFile
        fields = '__all__'


class VisualizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visualization
        fields = '__all__'


class DashboardSerializer(serializers.ModelSerializer):
    csv_files = CSVFileSerializer(many=True, read_only=True)
    visualizations = VisualizationSerializer(many=True, read_only=True)

    class Meta:
        model = Dashboard
        fields = ['id', 'name', 'owner', 'organization', 'created_at', 'qr_code_url', 'csv_files', 'visualizations']
