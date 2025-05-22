# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, permissions
# from django.shortcuts import render
# from rest_framework import viewsets, permissions
# from .models import (
#     Organization, CustomUser, Dashboard,
#     CSVFile, Visualization
# )
# from .serializers import (
#     OrganizationSerializer, UserSerializer, DashboardSerializer,
#     CSVFileSerializer, VisualizationSerializer
# )

# class OrganizationViewSet(viewsets.ModelViewSet):
#     queryset = Organization.objects.all()
#     serializer_class = OrganizationSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAdminUser]  # or customize


# class DashboardViewSet(viewsets.ModelViewSet):
#     queryset = Dashboard.objects.all()
#     serializer_class = DashboardSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class CSVFileViewSet(viewsets.ModelViewSet):
#     queryset = CSVFile.objects.all()
#     serializer_class = CSVFileSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class VisualizationViewSet(viewsets.ModelViewSet):
#     queryset = Visualization.objects.all()
#     serializer_class = VisualizationSerializer
#     permission_classes = [permissions.IsAuthenticated]


# User = get_user_model()

# class RegisterView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
        
#         if serializer.is_valid():
#             # Explicitly save the user
#             user = User.objects.create_user(
#                 email=serializer.validated_data['email'],
#                 username=serializer.validated_data['username'],
#                 password=serializer.validated_data['password']
#             )
#             return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # Create your views here.
