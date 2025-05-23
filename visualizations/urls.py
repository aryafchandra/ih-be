from django.urls import path
from .views import create_visualization, get_dashboard_visualizations, visualization_detail

urlpatterns = [
    path('', create_visualization, name='create-visualization'),  # POST
    path('dashboard/<int:dashboard_id>/', get_dashboard_visualizations, name='get-dashboard-visualizations'),
    path('<int:pk>/', visualization_detail, name='visualization-detail'),  
]
