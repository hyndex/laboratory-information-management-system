from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt

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
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Module_created_by', blank=True,null=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Module_updated_by', blank=True,null=True)
    
    def __str__(self):
        return self.module

class Role(models.Model):
    role = models.CharField(max_length=50)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Role_created_by', blank=True,null=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Role_updated_by', blank=True,null=True)
    
    def __str__(self):
        return self.role

class RolePermission(models.Model):
    TYPE_CHOICES = (('FullAccess','FullAccess'),('ReadOnly','ReadOnly'),('OnlyOwner','OnlyOwner'),('OnlyCreated','OnlyCreated'),('OnlySuperAdmin','OnlySuperAdmin'))
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    create = models.BooleanField(default=False)
    read = models.BooleanField(default=True)
    update = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    type = models.CharField(max_length=50, default='ReadOnlyTree',choices=TYPE_CHOICES)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='RolePersission_created_by', blank=True,null=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='RolePersission_updated_by', blank=True,null=True)


    def __str__(self):
        return str(self.role.role)

class ProfileRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='ProfileRole_created_by', blank=True,null=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='ProfileRole_updated_by', blank=True,null=True)
    
