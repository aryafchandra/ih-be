from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Dashboard
from .serializers import DashboardSerializer

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
