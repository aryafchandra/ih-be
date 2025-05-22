from django.urls import path
from .views import create_visualization, get_dashboard_visualizations

urlpatterns = [
    path('create/', create_visualization, name='create-visualization'),
    path('dashboard/<int:dashboard_id>/', get_dashboard_visualizations, name='get-dashboard-visualizations'),
]
