from users.custom import *
from .views import *

pre_append='api/'
post_append='<int:role>/<int:section>/'
optional_append='<int:id>/'

views['section']=SectionView.as_view()
views['test']=TestView.as_view()
views['client']=ClientView.as_view()
views['sample']=SampleView.as_view()
views['sample_test']=SampleTestView.as_view()


urlpatterns = make_url_pattern(views,pre_append,post_append,optional_append)