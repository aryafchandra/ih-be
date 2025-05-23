from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import DashboardSerializer
from django.shortcuts import get_object_or_404
from .models import Dashboard
from .serializers import DashboardSerializer
import csv

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_dashboard(request):
    serializer = DashboardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_dashboards(request):
    dashboards = Dashboard.objects.filter(user=request.user)
    serializer = DashboardSerializer(dashboards, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_dashboard_detail(request, id):
    dashboard = get_object_or_404(Dashboard, pk=id, user=request.user)
    serializer = DashboardSerializer(dashboard)

    csv_data = None
    csv_fields = []
    if dashboard.csv:
        try:
            with open(dashboard.csv.file.path, newline='') as f:
                reader = csv.DictReader(f)
                csv_data = list(reader)
                csv_fields = reader.fieldnames
        except Exception as e:
            print(f"Error reading CSV file for dashboard {id}: {e}")

    data = serializer.data
    data['csvfile'] = data.get('csvfile', {})
    data['csvfile']['data'] = csv_data
    data['csvfile']['fields'] = csv_fields

    return Response(data)