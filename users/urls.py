from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'Profile', ProfileViewSet)
router.register(r'RolePermission', RolePermissionViewSet)
router.register(r'Role', RoleViewSet)
router.register(r'ProfileRole', ProfileRoleViewSet)
router.register(r'RolePermission', RolePermissionViewSet)
# router.register(r'User', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('ChangePassword/', ChangePasswordView.as_view()),
    path('Permission/', PermissionView),
    path('Install/', InstallView),
    path('Logout/', LogoutView.as_view()),
    path('Login/', LoginView.as_view()),
    path('CreateUser/', CreateUserView.as_view()),
]