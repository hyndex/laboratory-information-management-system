from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt

class Section(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    description = models.CharField(max_length=50, blank=False, null=True, default = '')
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Section_created_by', blank=True,null=True)
    updated = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Section_updated_by', blank=True,null=True)
    def __str__(self):
        return self.name
    @property
    def tests(self):
        return self.test_set.all() 

class Test(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='test_section')
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    description = models.CharField(max_length=50, blank=False, null=True, default = '')
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Test_created_by', blank=True,null=True)
    updated = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Test_updated_by', blank=True,null=True)
    def __str__(self):
        return self.section.name+'->'+self.name 
    # @property
    # def fields(self):
    #     return self.field_set.all()
    # @property
    # def section_id(self):
    #     return self.section.id

class Field(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='field_test')
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    formula = models.CharField(max_length=500, blank=False, null=True,default='')
    measure = models.CharField(max_length=50, blank=False, null=True, default='')
    uplimit = models.FloatField(default = 0)
    downlimit = models.FloatField(default = 0)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Field_created_by', blank=True,null=True)
    updated = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Field_updated_by', blank=True,null=True)
    def __str__(self):
        return self.test.name+'-'+self.name 
    @property
    def fields(self):
        return self.field_set.all()
    
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    phone = models.CharField(max_length=20, blank=False, null=True, default = '')
    address = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to='profile/',blank=True, null=True)    
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Client_created_by', blank=True,null=True)
    updated= models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Client_updated_by', blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    @property
    def samples(self):
        return self.sample_set.all()

class Sample(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, blank=False, null=True, default = '')
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Sample_created_by', blank=True,null=True)
    updated = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Sample_updated_by', blank=True,null=True)
    def __str__(self):
        return self.name
    
    @property
    def sampletests(self):
        return self.sampletest_set.all()


class SampleTest(models.Model):
    TYPE_CHOICES = (('Created','Created'),('Progress','Progress'),('Finished','Finished'))
    sample = models.ForeignKey(Sample, on_delete=models.PROTECT,  related_name='SampleTest_sample')
    test = models.ForeignKey(Test, on_delete=models.PROTECT,  related_name='SampleTest_test')
    test_status = models.CharField(max_length=15, default='Created',choices=TYPE_CHOICES)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='SampleTest_created_by', blank=True,null=True)
    updated = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='SampleTest_updated_by', blank=True,null=True)
    def __str__(self):
        return self.sample.name
    
    @property
    def resultfield(self):
        return self.resultfields_set.all()


class ResultFields(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE,related_name='ResultFields_field')
    sample_test = models.ForeignKey(SampleTest, on_delete=models.CASCADE,related_name='ResultFields_sample_test')
    value = models.FloatField(default=0)
    reason = models.CharField(max_length=50, blank=False, null=True, default = '')
    note = models.CharField(max_length=150, blank=False, null=True, default = '')
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='ResultFields_created_by', blank=True,null=True)
    updated = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='ResultFields_updated_by', blank=True,null=True)
    # def __str__(self):
    #     return self.


class Product(models.Model):
    name = models.CharField(max_length=150, blank=False, null=True, default = '')
    formula = models.CharField(max_length=150, blank=False, null=True, default = '')
    measure = models.CharField(max_length=50, blank=False, null=True, default = '')
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Product_created_by', blank=True,null=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Product_updated_by', blank=True,null=True)
    def __str__(self):
        return self.name+'->'++self.measure


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True,null=True)
    quantity = models.FloatField(default=0)
    unit = models.FloatField(default=0)
    measure = models.CharField(max_length=50, blank=False, null=True, default = '')
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Inventory_created_by', blank=True,null=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='Inventory_updated_by', blank=True,null=True)
    def __str__(self):
        return self.product.name+'->'+self.quantity+'->'+self.unit+' '+self.product.measure

