from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Visualization
from .serializers import VisualizationSerializer
from django.shortcuts import get_object_or_404

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_visualization(request):
    serializer = VisualizationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_dashboard_visualizations(request, dashboard_id):
    visualizations = Visualization.objects.filter(dashboard__id=dashboard_id)
    serializer = VisualizationSerializer(visualizations, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def visualization_detail(request, pk):
    visualization = get_object_or_404(Visualization, pk=pk)
    
    if request.method == 'PUT':
        serializer = VisualizationSerializer(visualization, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

