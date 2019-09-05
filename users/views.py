from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from users.permissions import *
# from .models import *
from .serializers import *



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model=serializer_class().Meta().model
    permission_classes = [CustomPermission]
    def get_queryset(self):
        print(self.request.user)
        return get_query(self.request,self.model).queryset()

# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [CustomPermission]
#     model=serializer_class().Meta().model
#     def get_queryset(self):
#         print(self.request.user)
#         return get_query(self.request,self.model).queryset()


class RolePermissionViewSet(viewsets.ModelViewSet):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer
    permission_classes = [CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        print(self.request.user)
        return get_query(self.request,self.model).queryset()

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        print(self.request.user)
        return get_query(self.request,self.model).queryset()


class ProfileRoleViewSet(viewsets.ModelViewSet):
    queryset = ProfileRole.objects.all()
    serializer_class = ProfileRoleSerializer
    permission_classes = [CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        print(self.request.user)
        return get_query(self.request,self.model).queryset()


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        print(self.request.user)
        return get_query(self.request,self.model).queryset()


class ChangePasswordView(UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                return Response("Success.", status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CreateUserView(CreateAPIView):
#     model = User()
#     permission_classes = [CustomPermission]
#     serializer_class = UserSerializer
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)# if data is not valid then will not proceed forward and return a error msg
        user = serializer.validated_data['user']
        django_login(request,user)
        token, created=Token.objects.get_or_create(user=user)#created = True if token already exist else False
        return Response({"token": token.key },status=200)
    
class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    def post(self, request):
        django_logout(request)
        #if not multiple browsers then delete from token table 
        return Response({"msg":"successfully logout"},status=204)

def PermissionView(request):
    import json
    if request.user.is_authenticated:
        perm=fundamental().user_role_permission(username=str(request.user))
        return JsonResponse(perm,safe=False)
    else:
        return Response({"msg":"Not LoggedIn"},status=400)

from  users.install import *
def InstallView(request):
    msg=install().install()
    return JsonResponse(msg,safe=False)