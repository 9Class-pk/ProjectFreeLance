
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
    ProjectListAPIVIew,
    ProjectDetailAPIVIew,
    MyProjectsView,
    OfferViewSet,
    ReviewViewSet,
    RegisterView,
    LoginView,
    LogoutView
)

router = DefaultRouter()
router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'offers', OfferViewSet, basename='offer')
router.register(r'reviews', ReviewViewSet, basename='review')

app_name = 'projects'

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/me', CurrentUserAPIView.as_view(), name='current_user'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('projects/', ProjectListAPIVIew.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailAPIVIew.as_view(), name='project_detail'),
    path('projects/my/', MyProjectsView.as_view(), name='my_project')


]