from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
from users.models import *


class FieldSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Field
        fields='__all__'
        read_only_fields=('date_updated','created_by','updated_by')    


class TestSerializer(serializers.ModelSerializer):
    field = FieldSerializer(many=True)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Test
        fields=['id','module','name','description','field','date_updated','created_by','updated_by']
        read_only_fields=('date_updated','created_by','updated_by')  
          

class SectionSerializer(serializers.ModelSerializer):
    test=TestSerializer(many=True)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Section
        fields=['id','name','description','test','date_updated','created_by','updated_by']
        read_only_fields=('date_updated','created_by','updated_by')    

class SampleTestStatusSerializer(serializers.ModelSerializer):
    # fields=ResultFieldsSerializer(many=True)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = SampleTestStatus
        fields=['test_status','field_type','date_updated','created_by','updated_by']
        read_only_fields=('date_updated','created_by','updated_by')   


class ResultFieldsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = ResultFields
        fields='__all__'
        read_only_fields=('date_updated','created_by','updated_by')   


class SampleTestSerializer(serializers.ModelSerializer):
    fields=ResultFieldsSerializer(many=True)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = SampleTest
        fields=['sample','test','fields','date_updated','created_by','updated_by']
        read_only_fields=('date_updated','created_by','updated_by')    
 
class SampleSerializer(serializers.ModelSerializer):
    test=TestSerializer(many=True)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Sample
        fields=['client','name','test','date_updated','created_by','updated_by']
        read_only_fields=('date_updated','created_by','updated_by')   

class ClientSerializer(serializers.ModelSerializer):
    sample=SampleSerializer(many=True)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Client
        fields=['user','name','phone','address','status','image','sample','date_updated','created_by','updated_by']
        read_only_fields=('date_updated','created_by','updated_by')    
