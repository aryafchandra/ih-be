# users/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.http import require_POST, require_GET
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import RegisterAnalystSerializer, AnalystSerializer
from users.models import Analyst
from .services.registration import register_analyst
from .services.login import login_analyst
import json

@require_POST
@api_view(['POST'])
@permission_classes([AllowAny])
def serve_register_analyst(request):
    """
        request_data must contain:
        email, password, confirmed_password, first_name, last_name (optional), phone_number, employee_id (optional)
    """
    request_data = json.loads(request.body.decode('utf-8'))
    try:
        analyst = register_analyst(request_data)
        refresh = RefreshToken.for_user(analyst)
        response_data = {
            'user': AnalystSerializer(analyst).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return Response(data=response_data, status=201)
    except Exception as e:
        return Response({'detail': str(e)}, status=400)

@require_POST
@api_view(['POST'])
def serve_login_analyst(request):
    """
        request_data must contain:
        email, password
    """
    request_data = json.loads(request.body.decode('utf-8'))
    try:
        token = login_analyst(request_data)  # <-- move logic to service layer
        return Response(data=token, status=200)
    except Exception as e:
        return Response({'detail': str(e)}, status=401)

@require_GET
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def serve_get_user_info(request):
    return Response(data=AnalystSerializer(request.user).data)