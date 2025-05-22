# users/serializers.py
from rest_framework import serializers
from users.models import Analyst

class RegisterAnalystSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyst
        fields = ['email', 'password', 'first_name', 'last_name', 'phone_number', 'employee_id']
        extra_kwargs = {'password': {'write_only': True}}

class AnalystSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyst
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'employee_id']
