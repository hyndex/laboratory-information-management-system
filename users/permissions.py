from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from users.models import *

def user_role_permission(username):
    try:
        my_methods=['GET','POST','PUT','DELETE']
        profile_roles = ProfileRole.objects.filter(user__user__username=username)
        roles = {}
        for profile_role in profile_roles:
            role_perm=RolePermission.objects.filter(role=profile_role.role)
            model_perm = {}
            for permission_set in role_perm:
                module = Module.objects.get(id=permission_set.module_id).module
                model_perm[module] = {}
                model_perm[module]['module_id'] = permission_set.module_id
                model_perm[module]['create'] = permission_set.create
                model_perm[module]['read'] = permission_set.read
                model_perm[module]['update'] = permission_set.update
                model_perm[module]['delete'] = permission_set.delete
                model_perm[module]['type'] = permission_set.type
                model_perm[permission_set.module_id]['scope'] = permission_set.scope
            roles = {}
            roles['role_name']=profile_role.role.role
            roles['role_id']=profile_role.role.id
            roles['permissions']=model_perm
        return roles
    except Exception as e:
        return e  

from rest_framework.permissions import BasePermission

class AdminOnly(BasePermission):
    message='You are not authorized to access this page'
    def has_permission(self, request, view):
        # return (request.user == 'Admin')or(request.user=='admin')
        if ProfileRole.objects.filter(user__user__username=request.user,role__role='Admin').count() >0:
            return True