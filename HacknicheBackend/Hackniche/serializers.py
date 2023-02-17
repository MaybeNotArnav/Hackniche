from .models import SiteUser
from rest_framework import serializers
from django.contrib.auth.models import User

class SiteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteUser
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['email','username','password']