from rest_framework import serializers
from users.models import *
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

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


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Profile
        fields = ('id','user','name','phone','address','status','image',)
        read_only_fields=('user',)

class UserSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer(required=True)
    class Meta:
        model = User
        fields=('id','username','password','email','profile')
        write_only_fields=('password',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(username=user_data['username'],
                            email=user_data['email'],
                            )
        user.set_password(user_data['password'])
        user.save()
        profile = Profile.objects.create(user=user,
                            phone=validated_data.pop('phone'),
                            name=validated_data.pop('name'),
                            address=validated_data.pop('address'),
                            status=validated_data.pop('status'),
                            image=validated_data.pop('image'),
                            )
        return profile

    def update(self, instance ,validated_data):
        profiles = validated_data.pop('profile')
        instance.email=validated_data.get('email',instance.email)
        instance.save()
        # existing_ids=[u.id for u in instance.user]
        if 'id' in profiles.keys():
            if Profile.objects.filter(id=profiles['id']).exists():
                p=Profile.objects.get(id=profiles['id'])
                p.name=profiles.get('name',p.name)
                p.phone=profiles.get('phone',p.phone)
                p.address=profiles.get('address',p.address)
                p.status=profiles.get('status',p.status)
                p.image=profiles.get('image',p.image)
                p.save()
        return instance
    

class RolePermissionSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)
    class Meta:
        model = RolePermission
        fields=('id','module','role','create','read','update','delete','type','date_updated','created_by','updated_by')
        read_only_fields=('date_updated','created_by','updated_by')


class RoleSerializer(serializers.ModelSerializer):
    rolepermission_role = RolePermissionSerializer(many=True)
    class Meta:
        model = Role
        fields=('id','role','date_updated','created_by','updated_by','rolepermission_role')
        read_only_fields=('date_updated','created_by','updated_by')

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields='__all__'
        read_only_fields=('date_updated','created_by','updated_by')

class ProfileRoleSerializer(serializers.ModelSerializer):
    # role=RoleSerializer(required=True)
    # profile=ProfileSerializer(required=True)
    class Meta:
        model = ProfileRole
        fields=('id','user','role','scope','depertment','date_updated','created_by','updated_by')
        read_only_fields=('date_updated','created_by','updated_by')
             

