from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.views import APIView
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
#from users.permissions import *
from rest_framework.permissions import *
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins

   
class CreateUserView(CreateAPIView):
    model = User()
    permission_classes = [
        AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

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
    
 
class RolePermissionView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    
    model=RolePermission
    serializer=RolePermissionSerializer
    queryset = model.objects.all()
    serializer_class = serializer
    lookup_field='id'
    filter_fields='__all__'
    ordering_fields='__all__'
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProfileRoleView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    
    model=ProfileRole
    serializer=ProfileRoleSerializer
    queryset = model.objects.all()
    serializer_class = serializer
    lookup_field='id'
    filter_fields='__all__'
    ordering_fields='__all__'
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class ProfileView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    
    model=Profile
    serializer=ProfileSerializer
    queryset = model.objects.all()
    serializer_class = serializer
    lookup_field='id'
    #filter_fields='__all__'
    ordering_fields='__all__'
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)