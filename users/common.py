from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from users.permissions import *
import sys
from users.models import *
from lims.models import *

class fundamental():
    def str_to_class(self,classname):
        return getattr(sys.modules[__name__], classname)
    def get_class_name(self,classobj):
        return classobj.__name__
    def get_model_id(self,classobj):
        class_name=self.get_class_name(classobj)
        return Module.objects.filter(module=class_name)[0].id
    def get_role_id(self,username):
        return ProfileRole.objects.filter(user__user__username=username)[0].role_id
    def get_role_name(self,username):
        return ProfileRole.objects.filter(user__user__username=username)[0].role.role
    def get_model_fields(self,model):
        return model._meta.fields
    def user_role_permission(self,username):
        try:
            profile_role = ProfileRole.objects.filter(user__user__username=username)[0]
            roles = {}
            role_perm=RolePermission.objects.filter(role=profile_role.role)
            model_perm = {}
            for permission_set in role_perm:
                module = Module.objects.get(id=permission_set.module_id).module
                model_perm[permission_set.module_id] = {}
                model_perm[permission_set.module_id]['module'] = module
                model_perm[permission_set.module_id]['create'] = permission_set.create
                model_perm[permission_set.module_id]['read'] = permission_set.read
                model_perm[permission_set.module_id]['update'] = permission_set.update
                model_perm[permission_set.module_id]['delete'] = permission_set.delete
                model_perm[permission_set.module_id]['type'] = permission_set.type
                # model_perm[permission_set.module_id]['scope'] = permission_set.scope
            roles = {}
            roles['role_name']=fundamental().get_role_name(username)
            roles['permissions']=model_perm
            return roles
        except Exception as e:
            return e  
    def get_all_models(self):
        module_dict = {}
        for module in Module.objects.all():
            module_dict[module.module]=fundamental().str_to_class(module.module)
        return module_dict
    
    def skip_check(self,view,request):
        try:
            if (view.read in [True,False] and view.id) and str(request.method) == 'GET':
                return view.read
        except:
            pass
        try:
            if view.list in [True,False] and str(request.method) == 'GET':
                return view.list
        except:
            pass
        try:
            if view.create in [True,False] and str(request.method) == 'POST':
                return view.create
        except:
            pass
        try:
            if view.update in [True,False] and str(request.method) == 'PUT':
                return view.update
        except:
            pass
        try:
            if view.delete == True and str(request.method) == 'DELETE':
                return view.delete
        except:
            pass
        return None