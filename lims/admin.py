from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Section)
admin.site.register(Test)
admin.site.register(Field)
admin.site.register(Client)
admin.site.register(Sample)
admin.site.register(SampleTest)
admin.site.register(ResultFields)
admin.site.register(SampleTestStatus)
