import re

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_phone_number(phone):
    return re.match(r"^\\+?\\d{7,15}$", phone)

def validate_password(password):
    return len(password) >= 8  # Simplified — you can expand this
