from django.urls import path
from .views import serve_register_analyst, serve_login_analyst

urlpatterns = [
    path('register/', serve_register_analyst, name='serve-register-analyst'),
    path('login/', serve_login_analyst, name='serve-login-analyst'),
]