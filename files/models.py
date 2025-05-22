from django.db import models
from django.contrib.auth import get_user_model

class CSV(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='csv_uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='csv_files', null=True)

    def __str__(self):
        return self.name
