from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from users.models import *

from django.contrib import admin
from django.urls import path
from django.urls import include, path
from users.views import *
from rest_framework import routers

def make_url_pattern(view,pre_append='',post_append='',optional_append=''):
    pre_append='api/'
    post_append='<int:owner>/<int:role>/'
    optional_append='<int:id>/'
    urlpatterns=[]
    for key in view.keys():
        urlpatterns.append(path(pre_append+key+'/'+post_append,view[key]))
        if not optional_append=='':
            urlpatterns.append(path(pre_append+key+'/'+post_append+optional_append,view[key]))
    return urlpatterns
views={}
