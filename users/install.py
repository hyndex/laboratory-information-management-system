def install():
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
install()

# Module.objects.all().delete()
# User.objects.all().delete()
# Profile.objects.all().delete()
# Role.objects.all().delete()
# RolePermission.objects.all().delete()
# ProfileRole.objects.all().delete()