from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from .models import *
from users.models import *


class FieldSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)
    class Meta:
        model = Field
        fields=('test_id','name','formula','measure','uplimit','downlimit',"date_updated","created_by","updated_by")
        read_only_fields=("date_updated","created_by","updated_by")    


class TestSerializer(serializers.ModelSerializer):
    field_test = FieldSerializer(many=True,required=True)
    # id = serializers.IntegerField(required=False)
    class Meta:
        model = Test
        fields=["id","section_id","name","description","field_test","date_updated","created_by","updated_by"]
        read_only_fields=('section',"date_updated","created_by","updated_by")  
        depth = 1
        
          

class SectionSerializer(serializers.ModelSerializer):
    test_module=TestSerializer(many=True,required=False)
    class Meta:
        model = Section
        fields=["id","name","description","test_module","date_updated","created_by","updated_by"]
        read_only_fields=("date_updated","created_by","updated_by")
        depth = 1
    

class SampleTestStatusSerializer(serializers.ModelSerializer):
    # fields=ResultFieldsSerializer(many=True)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = SampleTestStatus
        fields=["test_status","field_type","date_updated","created_by","updated_by"]
        read_only_fields=("date_updated","created_by","updated_by")   


class ResultFieldsSerializer(serializers.ModelSerializer):
    # ResultFields_field=FieldSerializer(many=True,required=False)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = ResultFields
        fields=('field','sample_test_id','value','reason','note',"date_updated","created_by","updated_by")
        read_only_fields=('field','sample_test',"date_updated","created_by","updated_by")   
        depth=1


class SampleTestSerializer(serializers.ModelSerializer):
    ResultFields_field=ResultFieldsSerializer(many=True,required=False)
    # id = serializers.IntegerField(required=False)
    class Meta:
        model = SampleTest
        fields=["sample_id","test_id","fields",'ResultFields_field',"date_updated","created_by","updated_by"]
        read_only_fields=("date_updated","created_by","updated_by")  
        depth=1  
 
class SampleSerializer(serializers.ModelSerializer):
    SampleTest_sample=SampleTestSerializer(many=True)
    class Meta:
        model = Sample
        fields=["client","name","test",'SampleTest_sample',"date_updated","created_by","updated_by"]
        read_only_fields=("date_updated","created_by","updated_by")   
        depth=1

class ClientSerializer(serializers.ModelSerializer):
    # sample=SampleSerializer(many=True)
    class Meta:
        model = Client
        fields='__all__'
        read_only_fields=("date_updated","created_by","updated_by")   
        depth=1 
