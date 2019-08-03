from rest_framework import serializers
from .models import *
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username','')
        password = data.get('password','')

        if username and password:#checking if both are avalable or not
            user = authenticate(username=username,password=password)
            if user:# if user found 
                if user.is_active:# if user is active
                    data['user'] = user #if all correct then we are going to add "user" to given "data" and return 
                else:#if account is not active reise or active the account
                    msg = 'account is not active'
                    raise exceptions.ValidationError(msg)
            else:
                msg = 'unable to login with given creds'
                raise exceptions.ValidationError(msg)
        else:
            msg = 'Username or Passwords are both required !!!'
            raise exceptions.ValidationError(msg)
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username','password','email')
        write_only_fields=('password',)

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Profile
        fields = ('user','name','phone','address','status','image',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(username=user_data['username'],
                            email=user_data['email'],
                            )
        user.set_password(user_data['password'])
        user.save()
        profile = Profile.objects.create(user=user,
                            phone=validated_data.pop('phone'),
                            address=validated_data.pop('address'),
                            status=validated_data.pop('status'),
                            image=validated_data.pop('image'),
                            )
        return profile


class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields='__all__'
        read_only_fields=('date_updated','created_by','updated_by')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields='__all__'
        read_only_fields=('date_updated','created_by','updated_by')


class ProfileRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileRole
        fields='__all__'
        read_only_fields=('date_updated','created_by','updated_by')
             

