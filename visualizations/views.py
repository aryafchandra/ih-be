from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Visualization
from .serializers import VisualizationSerializer

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
