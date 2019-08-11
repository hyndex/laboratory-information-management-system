from users.common import *
import django

class install():
    def install(self):
        msg='{"Already installed"}'
        apps=['lims','users']
        models=[]
        for app in apps:
            models+=[model.__name__ for model in django.apps.apps.all_models[app].values()]
        if Module.objects.count() == 0:
            for model in models:
                Module(module=model).save()
                print(model)

            User.objects.create_user('admin', password='qwerty',is_staff=True,is_superuser=True)
            Profile(user=User.objects.get()).save()

            Role(role='Admin').save()

            role=Role.objects.get()
            for model in Module.objects.all():
                RolePermission(module=model,role=role,create=True,read=True,update=True,delete=True).save()

                
            ProfileRole(user=Profile.objects.get(),role=Role.objects.get()).save()
            
            
            sampleteststatus='SampleTestStatus.objects.filter(test__section__id=self.section_id)'
            resultfield='ResultFields.objects.filter(test__section__id=self.section_id)'
            field='Field.objects.filter(test__section__id=self.section_id)'
            test='Test.objects.filter(section__id=self.section_id)'
            
            def module(name):
                return Module.objects.get(module=name)
            Scope(scope_module=module('Section'),module=module('Test'),query_set=test).save()
            Scope(scope_module=module('Section'),module=module('ResultFields'),query_set=resultfield).save()
            Scope(scope_module=module('Section'),module=module('Field'),query_set=field).save()
            Scope(scope_module=module('Section'),module=module('SampleTestStatus'),query_set=sampleteststatus).save()
            msg='{"Installation Done"}'
        return msg

# print(Module.objects.all().delete())
# print(User.objects.all().delete())
# print(Profile.objects.all().delete())
# print(Role.objects.all().delete())
# print(RolePermission.objects.all().delete())
# print(ProfileRole.objects.all().delete())
# print(Scope.objects.all().delete())