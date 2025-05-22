from users.models import Analyst
from . import utils
from insighthub_backend.exceptions import InvalidRegistrationException
import datetime

def register_analyst(request_data):
    validate_analyst_registration_data(request_data)
    analyst = save_analyst_from_request_data(request_data)
    return analyst

def validate_analyst_registration_data(data):
    email = data.get('email', '').lower()
    password = data.get('password')
    confirm_password = data.get('confirmed_password')
    phone_number = data.get('phone_number')

    if not email:
        raise InvalidRegistrationException("Email must not be null.")
    if not utils.validate_email(email):
        raise InvalidRegistrationException("Email is invalid.")
    if Analyst.objects.filter(email=email).exists():
        raise InvalidRegistrationException(f"Email {email} is already registered.")
    if not password:
        raise InvalidRegistrationException("Password must not be null.")
    if password != confirm_password:
        raise InvalidRegistrationException("Password and confirmation do not match.")
    if not utils.validate_password(password):
        raise InvalidRegistrationException("Password does not meet complexity requirements.")
    # if not phone_number or not utils.validate_phone_number(phone_number):
    #     raise InvalidRegistrationException("Invalid or missing phone number.")

def save_analyst_from_request_data(data):
    return Analyst.objects.create_user(
        email=data['email'],
        password=data['password'],
        first_name=data.get('first_name', ''),
        last_name=data.get('last_name', ''),
        phone_number=data['phone_number'],
        employee_id=data.get('employee_id', '')
    )
