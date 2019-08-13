from django.contrib.auth.models import User, Group
from rest_framework import serializers
from users.permissions import *
# from .models import *
from users.models import *


class FieldSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Field
        fields=('id','test_id','name','formula','measure','uplimit','downlimit',"date_updated","created","updated")
        read_only_fields=("date_updated","created","updated")    


class TestSerializer(serializers.ModelSerializer):
    field_test = FieldSerializer(many=True,required=True)
    section_id=serializers.IntegerField(write_only=True)
    # id = serializers.IntegerField(required=False)
    class Meta:
        model = Test
        fields=["id","section",'section_id',"name","description","field_test","date_updated","created","updated"]
        read_only_fields=("date_updated","created","updated")  
        depth = 1
        
    def create(self, validated_data):
        fields = validated_data.pop('field_test')
        section=get_query(self.context['request'],Section).queryset().filter(id=validated_data.get('section_id'))[0]
        print(section)
        validated_data['created']=self.context['request'].user
        test=Test.objects.create(**validated_data,section=section)
        for field in fields:
            Field.objects.create(**field,test=test)
        return test   

    def update(self, instance, validated_data):
        fields=validated_data.pop('field_test')
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.save()
        keep_fields=[]
        Field_set=Field.objects.filter(test__id=instance.id)
        existing_ids=[f.id for f in Field_set]
        for field in fields:
            if 'id' in field.keys():
                if Field.objects.filter(id=field['id']).exists():
                    f=Field.objects.get(id=field['id'])
                    f.name=field.get('name',f.name)
                    f.formula=field.get('formula',f.formula)
                    f.measure=field.get('measure',f.measure)
                    f.uplimit=field.get('uplimit',f.uplimit)
                    f.downlimit=field.get('downlimit',f.downlimit)
                    f.updated=self.context['request'].user
                    f.save()
                    keep_fields.append(f.id)
                else:
                    continue
            else:
                f=Field.objects.create(**field,test=instance)  
                keep_fields.append(f.id)
        print('instance id ',(instance.id))
        print('keep field id ',keep_fields)
        print(Field_set)
        for field in Field_set:
            if field.id not in keep_fields:
               field.delete()
        return instance

class SectionSerializer(serializers.ModelSerializer):
    test_section=TestSerializer(many=True,read_only=True)
    class Meta:
        model = Section
        fields=["id","name","description","test_section","date_updated","created","updated"]
        read_only_fields=("test_section","date_updated","created","updated")
        depth = 1
    
##testing required for forignkey enablation
class ResultFieldsSerializer(serializers.ModelSerializer):
    # ResultFields_field=FieldSerializer(many=True,required=False)
    id = serializers.IntegerField(required=False,read_only=True)
    class Meta:
        model = ResultFields
        fields=('id','value','reason','note',"date_updated","created","updated")
        read_only_fields=("date_updated","created","updated")   
        # read_only_fields=('field','sample_test',"date_updated","created","updated")   
        depth=1
        
        

class SampleTestSerializer(serializers.ModelSerializer):
    sample_id = serializers.IntegerField(write_only=True)
    test_id = serializers.IntegerField(write_only=True)
    ResultFields_sample_test=ResultFieldsSerializer(many=True)
    class Meta:
        model = SampleTest
        # fields=["sample",'sample_id','test_id',"test",'ResultFields_sample_test',"date_updated","created","updated"]
        fields=['sample_id','test_id',"test",'test_status','ResultFields_sample_test',"date_updated","created","updated"]
        read_only_fields=('sample','test',"date_updated","created","updated")  
        depth=3  

    def create(self, validated_data):
        result_fields = validated_data.pop('ResultFields_sample_test')##waste

        sample=get_query(self.context['request'],Sample).queryset().filter(id=validated_data.get('sample_id'))[0]
        test=get_query(self.context['request'],Test).queryset().filter(id=validated_data.get('test_id'))[0]

        sample_test=SampleTest.objects.create(**validated_data,sample=sample,test=test,test_status='Created')

        fields=Field.objects.filter(test__id=test.id)
        if fields.exists():
            for field in fields:
                ResultFields.objects.create(field=field,sample_test=sample_test,created=self.context['request'].user)
        return sample_test

    def update(self, instance, validated_data):

        if instance.test_status == 'Created':
            instance.test_status='Progress'
        elif validated_data.get('test_status')=='Finished':
            instance.test_status='Finished'
        elif instance.test_status == 'Finished':
            return instance
        instance.save()

        result_fields=validated_data.pop('ResultFields_sample_test')
        keep_fields=[]
        ResultField_set=ResultFields.objects.filter(sample_test__id=instance.id)    
        existing_ids=[rf.id for rf in ResultField_set]
        for result_field in result_fields:
            if 'id' in result_field.keys():
                if ResultFields.objects.filter(id=result_field['id']).exists():
                    rf=ResultFields.objects.get(id=result_field['id'])
                    rf.value=result_field.get('value',rf.value)
                    rf.reason=result_field.get('reason',rf.reason)
                    rf.note=result_field.get('note',rf.note)
                    rf.updated=self.context['request'].user
                    rf.save()
                    keep_fields.append(rf.id)
                else:
                    continue
            # else:
            #     rf=ResultFields.objects.create(**result_fields,sample_test=instance)  
            #     keep_fields.append(rf.id)
        return instance

class SampleSerializer(serializers.ModelSerializer):
    SampleTest_sample=SampleTestSerializer(many=True,read_only=True)
    client_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Sample
        fields=["id","client",'client_id',"name",'SampleTest_sample',"date_updated","created","updated"]
        read_only_fields=('client',"date_updated","created","updated")   
        depth=1

    def create(self, validated_data):
        client=Client.objects.filter(id=validated_data.get('client_id'))[0]#get_query(self.context['request'],Sample).queryset().filter(id=validated_data.get('client_id'))[0]

        # sampleTest_sample = validated_data.pop('SampleTest_sample')
        sample=Sample.objects.create(**validated_data,client=client)
        return sample
    def update(self, instance, validated_data):
        return instance
        
class ClientSerializer(serializers.ModelSerializer):
    # sample=SampleSerializer(many=True)
    class Meta:
        model = Client
        fields='__all__'
        read_only_fields=("date_updated","created","updated")   
        depth=1 


