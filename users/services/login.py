from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import Analyst
from insighthub_backend.exceptions import InvalidLoginCredentialsException

def login_analyst(data):
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        raise InvalidLoginCredentialsException("Email and password must be provided.")

    user = authenticate(email=email, password=password)

    if user is None:
        raise InvalidLoginCredentialsException(f"Invalid credentials. email = {email}")

    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }
