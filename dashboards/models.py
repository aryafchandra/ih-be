from django.db import models
from django.conf import settings
from files.models import CSV

class Dashboard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    csv = models.ForeignKey(CSV, on_delete=models.CASCADE)  # removed null=True, blank=True
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
