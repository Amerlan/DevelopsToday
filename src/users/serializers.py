from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password1 = serializers.CharField(max_length=50)
    password2 = serializers.CharField(max_length=50)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise ValidationError('Passwords don’t match.')
        data.pop('password2')
        data['password'] = data.pop('password1')
        return data

    def create(self, validated_data):
        try:
            user = User(username=validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()
        except IntegrityError:
            raise ValidationError('Username is taken.')
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)