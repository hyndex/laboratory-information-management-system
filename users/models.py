from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt
from lims.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    phone = models.CharField(max_length=20, blank=False, null=True, default = '')
    address = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to='profile/',blank=True, null=True)    
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    
    def __str__(self):
        return self.user.username

class Module(models.Model):
    module = models.CharField(max_length=50)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Module_created', blank=True,null=True)
    updated = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Module_updated', blank=True,null=True)
    
    def __str__(self):
        return self.module
    # @property
    # def rolepermissions(self):
    #     return self.rolepermission_set.all() 

class Role(models.Model):
    role = models.CharField(max_length=50)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Role_created', blank=True,null=True)
    updated = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Role_updated', blank=True,null=True)
    
    def __str__(self):
        return self.role
    # @property
    # def rolepermissionroles(self):
    #     return self.rolepermissionrole_set.all() 


class Scope(models.Model):
    scope_module = models.ForeignKey(Module, on_delete=models.CASCADE,related_name='scope_scopemodule')#,default=Module.objects.filter(module='Section')[0])
    module = models.ForeignKey(Module, on_delete=models.CASCADE,related_name='scope_Module')
    query_set=models.TextField(blank=True, null=True)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Scope_created', blank=True,null=True)
    updated = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Scope_updated', blank=True,null=True)
    def __str__(self):
        return self.module.module+'_'+self.scope_module.module


class RolePermission(models.Model):
    TYPE_CHOICES = (('FullAccess','FullAccess'),('ReadOnly','ReadOnly'),('OnlyOwner','OnlyOwner'),('OnlyCreated','OnlyCreated'),('OnlySuperAdmin','OnlySuperAdmin'))
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='rolepermission_module')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='rolepermission_role')
    create = models.BooleanField(default=False)
    read = models.BooleanField(default=True)
    update = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    type = models.CharField(max_length=50, default='FullAccess',choices=TYPE_CHOICES)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='RolePersission_created', blank=True,null=True)
    updated = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='RolePersission_updated', blank=True,null=True)
    def __str__(self):
        return self.role.role+'->'+self.module.module

    # @property
    # def roles(self):
    #     return self.role_set.all() 


class ProfileRole(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='profilerole_profile')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='profilerole_role')
    depertment = models.ForeignKey(Section,on_delete=models.CASCADE, blank=True, null=True, related_name='profilerole_depertment')
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='ProfileRole_created', blank=True,null=True)
    updated = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='ProfileRole_updated', blank=True,null=True)
    def __str__(self):
        return self.user.user.username+'_'+self.role.role
    
    # @property
    # def profiles(self):
    #     return self.profile_set.all() 