from django.urls import path
from .views import create_dashboard, get_user_dashboards, get_dashboard_detail

urlpatterns = [
    path('create/', create_dashboard, name='create-dashboard'),
    path('my/', get_user_dashboards, name='get-user-dashboards'),
    path('<int:id>/', get_dashboard_detail, name='dashboard-detail'),
]
