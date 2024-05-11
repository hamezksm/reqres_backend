# registration/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserLoginViewSet, UserRegistrationViewSet
from .views import UserRegistrationViewSet, UserLoginViewSet

# create your urls here

router = DefaultRouter()
router.register(r'registration', UserRegistrationViewSet, basename='user-registration')
router.register(r'login', UserLoginViewSet, basename='user-login')

urlpatterns = router.urls
