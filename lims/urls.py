# from users.urlgen import *
from .views import *
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from users.views import *
from rest_framework import routers

def make_url_pattern(view,pre_append='',post_append='',optional_append=''):
    urlpatterns=[]
    for key in view.keys():
        urlpatterns.append(path(pre_append+key+'/'+post_append,view[key]))
        if not optional_append=='':
            urlpatterns.append(path(pre_append+key+'/'+post_append+optional_append,view[key]))
    return urlpatterns
views={}

pre_append=''
post_append=''
optional_append='<int:id>/'

views['section']=SectionView.as_view()
views['test']=TestView.as_view()
views['client']=ClientView.as_view()
views['sample']=SampleView.as_view()
views['sample_test']=SampleTestView.as_view()


urlpatterns = make_url_pattern(views,pre_append,post_append,optional_append)