from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'Section', SectionViewSet)
router.register(r'Test', TestViewSet)
# router.register(r'Field', FieldViewSet)
router.register(r'Client', ClientViewSet)
router.register(r'Sample', SampleViewSet)
router.register(r'SampleTest', SampleTestViewSet)
# router.register(r'ResultFields', ResultFieldsViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]