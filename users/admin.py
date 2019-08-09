from django.contrib import admin
from users.models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Module)
admin.site.register(Role)
admin.site.register(RolePermission)
admin.site.register(ProfileRole)
admin.site.register(Scope)
