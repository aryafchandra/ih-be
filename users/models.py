from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from enum import Enum
import uuid
from django.contrib.auth.base_user import BaseUserManager

# === Authentication Service Enum ===
class AuthenticationService(Enum):
    DEFAULT = 'default'

# === Custom User Manager ===
class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# === Base Custom User ===
class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.email

# class Organizaton(CustomUser):
#     company_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     company_name = models.CharField(max_length=50)
#     description = models.TextField(blank=True)
#     address = models.TextField(blank=True)

#     def get_analysts(self):
#         return self.analyst_set.all()

class Analyst(CustomUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    employee_id = models.CharField(max_length=50, blank=True, null=True)
    authentication_service = models.CharField(
        max_length=50,
        choices=[(tag.value, tag.value) for tag in AuthenticationService],
        default=AuthenticationService.DEFAULT.value
    )

    def dashboards(self):
        return self.dashboard_set.all()

    def datasets(self):
        return self.csvfile_set.all()
