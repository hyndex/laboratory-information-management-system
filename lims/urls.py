from users.custom import *
from .views import *

pre_append='api/'
post_append='<int:owner>/<int:role>/'
optional_append='<int:id>/'

# views['section']=CreateUserView.as_view()
# views['test']=InstituteView.as_view()
# views['client']=ProfileRoleView.as_view()
# views['sample']=ProfileView.as_view()
# views['sample_test']=ProfileView.as_view()


urlpatterns = make_url_pattern(views,pre_append,post_append,optional_append)