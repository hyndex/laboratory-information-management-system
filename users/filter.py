from users.common import *

class get_query(object):
    def queryset(self):
        module=self.model
        if not self.request.user.is_authenticated:
            print('#########user not logged in#########')
            return module.objects.none()
        self.section=ProfileRole.objects.get(user__user__username=self.username).depertment
        print(self.username,self.model_id)
        try:
            if self.section.id:
                query_set=Scope.objects.get(module__id=self.model_id).query_set
                self.section_id=self.section.id
                print('self.section_id',self.section_id)
                query_set='self.query_set='+query_set
                print(query_set)
                exec(query_set)
                return self.query_set
        except Exception as e:
            print(e)
            try:
                if self.section == None:
                    print('#########user has all perm#########')
                    return self.model.objects.all()
            except Exception as e:
                print(e)
                print('#########user not permitted#########')
                return self.model.objects.none()
            
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
            self.section=ProfileRole.objects.get(user__user__username=self.username).depertment
