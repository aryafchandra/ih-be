from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# # ENUM choices for user role
# USER_ROLES = (
#     ('admin', 'Admin'),
#     ('analyst', 'Analyst'),
#     ('viewer', 'Viewer'),
# )

# class Organization(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class CustomUser(AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="users")
#     role = models.CharField(max_length=10, choices=USER_ROLES, default='viewer')
#     is_active = models.BooleanField(default=True)  # Needed for auth compliance
#     email = models.EmailField(unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return f"{self.email} ({self.role})"


# class Dashboard(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=255)
#     owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='dashboards')
#     organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='dashboards')
#     created_at = models.DateTimeField(auto_now_add=True)
#     qr_code_url = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return self.name


# class CSVFile(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name="csv_files")
#     file = models.FileField(upload_to='csvs/')
#     original_filename = models.CharField(max_length=255)
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.original_filename


# class Visualization(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name='visualizations')
#     chart_type = models.CharField(max_length=50)
#     title = models.CharField(max_length=255)
#     config = models.JSONField()  # PostgreSQL-compatible
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

