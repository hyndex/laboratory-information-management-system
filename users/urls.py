from users.custom import *
from .views import *

pre_append='api/'
post_append=''
optional_append='<int:id>/'

views['register']=CreateUserView.as_view()
views['login']=LoginView.as_view()
views['logout']=LogoutView.as_view()
views['permission']=PermissionView
views['role_permission']=RolePermissionView.as_view()
views['profile_role']=ProfileRoleView.as_view()
views['profile']=ProfileView.as_view()


urlpatterns = make_url_pattern(views,pre_append,post_append,optional_append)