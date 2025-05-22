from django.db import models
from dashboards.models import Dashboard

class Visualization(models.Model):
    CHART_TYPES = [
        ('bar', 'Bar Chart'),
        ('line', 'Line Chart'),
        ('pie', 'Pie Chart'),
        ('scatter', 'Scatter Plot'),
        # Add more if needed
    ]

    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name='visualizations')
    title = models.CharField(max_length=100)
    chart_type = models.CharField(max_length=20, choices=CHART_TYPES)
    x_column = models.CharField(max_length=100)
    y_column = models.CharField(max_length=100)
    config = models.JSONField(blank=True, null=True)  # for additional chart configs

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.chart_type})"
