from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import BasePermission
from users.filter import *

class CustomPermission():
    def has_object_permission(self,request,view):
        if fundamental().skip_check(view,request) in [True,False]:
            return fundamental().skip_check(view,request) in [True,False]
        try:
            username=request.user.username
            module=view.model
            method=request.method
            module_id=fundamental().get_model_id(module)
            method_dict={'GET':'read','POST':'create','PUT':'update','DELETE':'delete'}
            method=method_dict[method]
            return fundamental().user_role_permission(username)['permissions'][module_id][method]
        except Exception as e:
            print(e)
            return False

    def has_object_permission(self, request, view, obj):
        try:
            pk=view.kwargs['pk']
            return queryset(request.user.username,view.model).filter(id=pk).count()>0
        except Exception as e:
            print(e)
            return False


class AdminOnly(BasePermission):
    message='You are not authorized to access this page'
    def has_permission(self, request, view):
        if ProfileRole.objects.filter(user__user__username=request.user,role__role='Admin').count() >0:
            return True

class IsOwnerProfile(BasePermission):
    message='You are not authorized to update this data'
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if str(request.method) in view.IsOwner_method:
            return obj.user.username == request.user.username
        # Instance must have an attribute named `owner`.
        return True

