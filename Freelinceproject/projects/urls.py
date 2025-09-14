
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)
from .views import (
    SkillViewSet,
    UserProfileListAPIView,
    UserProfileDetailAPIView,
    CurrentUserAPIView,
    CategoryViewSet,
    ProjectViewSet,
    OfferViewSet,
    ReviewViewSet,
    RegisterView,
    LoginView,
    LogoutView
)

router = DefaultRouter()
router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'offers', OfferViewSet, basename='offer')
router.register(r'reviews', ReviewViewSet, basename='review')

app_name = 'projects'

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/me', CurrentUserAPIView.as_view(), name='current_user'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),


]