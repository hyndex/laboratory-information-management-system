from users.common import *

class get_query(object):
    def __init__(self,request,model):
        self.model=model
        self.request=request
        self.model_name=fundamental().get_class_name(model)
        self.model_id=fundamental().get_model_id(model)
        self.method=request.method
        self.models=fundamental().get_all_models()
        if request.user.is_authenticated:
            self.user=request.user
            self.username=request.user.username
            self.role_id=fundamental().get_role_id(self.username)
            self.role_name=fundamental().get_role_name(self.username)

    def queryset(self):
        module=self.model
        module_id=fundamental().get_model_id(module)
        if not self.request.user.is_authenticated:
            print('############done###############')
            return module.objects.none()
        username=self.username
        print(username,module_id)
        try:
            if fundamental().user_role_permission(username)['permissions'][module_id]['scope'] == None:
                print('all')
                query_set=module.objects.all()
                return query_set
        except Exception as e:
            print(e)
            try:
                #check scope.filter_set, scope.value
                scope=fundamental().user_role_permission(username)['permissions'][module_id]['scope']
                scope_instance=scope#Scope.objects.get(id=scope.id)
                filter_set=scope_instance.filter_set
                exec('auto_value='+str(scope_instance.value))
                if isinstance(auto_value, str):
                    filter_string=filter_set+'='+'"'+auto_value+'"'
                str1=fundamental().get_class_name(module)+'.objects.filter('+filter_string+')'
                str1='query_set='+str1
                print(str1)
                exec(str1)
                return query_set
            except:
                query_set=module.objects.none()
                return query_set
                print('None')
        return query_set

