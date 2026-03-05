from typing import Any

from rest_framework import serializers
from accounts.models import User,Profile
from django.utils.translation import gettext_lazy as _
from django.core import exceptions
from django.contrib.auth.password_validation import validate_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class RegisterationSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(max_length=20,write_only=True)
    class Meta:
        model=User
        fields=['email','username','password','password1','is_active','is_staff']
    
    def validate(self, attrs):
        if attrs.get('password')!=attrs.get('password1'):
            raise serializers.ValidationError(
                {"detail":"password dosn't match!"}
            )
        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password":list(e.messages)})
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('password1')
        return super().create(validated_data)
    
    
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data= super().validate(attrs)
        data['email']=self.user.email
        data['username']=self.user.username
        data['user_id']=self.user.id
        
        return data


class ChangePasswordSerializer(serializers.Serializer):
    model=User
    old_password=serializers.CharField(required=True)
    new_password=serializers.CharField(required=True)
    new_password1=serializers.CharField(required=True)
    
    def validate(self, attrs):
        if attrs.get('new_password') != attrs.get('new_password1'):
            raise serializers.ValidationError({"detail":"Password dosn't match"})
        try:
            validate_password(attrs.get('new_password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password":list(e.messages)})
        
        return super().validate(attrs)
    
        
class ProfileSerializer(serializers.ModelSerializer):
    email=serializers.CharField(source='user.email',read_only=True)
    class Meta:
        model=Profile
        fields=['email','username','user_type','headline','bio','location','profile_picture']
        read_only_fields=['email']
        
        