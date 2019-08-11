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
from .models import *
from .serializers import *

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    model=serializer_class().Meta().model
    permission_classes = [IsAuthenticated,CustomPermission]
    def get_queryset(self):
        return get_query(self.request,self.model).queryset()


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.none()
    serializer_class = TestSerializer
    model=serializer_class().Meta().model
    permission_classes = [IsAuthenticated,CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        print(self.request.user.username, self.request.method, self.model)
        return get_query(self.request,self.model).queryset()

class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    model=serializer_class().Meta().model
    permission_classes = [IsAuthenticated,CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        print(self.request.user)
        return get_query(self.request,self.model).queryset()

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    model=serializer_class().Meta().model
    permission_classes = [IsAuthenticated,CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        print(self.request.user)
        return get_query(self.request,self.model).queryset()


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    model=serializer_class().Meta().model
    permission_classes = [IsAuthenticated,CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        print(self.request.user)
        return get_query(self.request,self.model).queryset()


class SampleTestViewSet(viewsets.ModelViewSet):
    queryset = SampleTest.objects.all()
    serializer_class = SampleTestSerializer
    model=serializer_class().Meta().model
    permission_classes = [IsAuthenticated,CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        print(self.request.user)
        return get_query(self.request,self.model).queryset()

class ResultFieldsViewSet(viewsets.ModelViewSet):
    queryset = ResultFields.objects.all()
    serializer_class = ResultFieldsSerializer
    model=serializer_class().Meta().model
    permission_classes = [IsAuthenticated,CustomPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        print(self.request.user)
        return get_query(self.request,self.model).queryset()
