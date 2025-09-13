
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import (
    SkillViewSet,
    UserProfileViewSet,
    CategoryViewSet,
    ProjectViewSet,
    OfferViewSet,
    ReviewViewSet,
)

router = DefaultRouter()
router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'users', UserProfileViewSet, basename='userprofile')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'offers', OfferViewSet, basename='offer')
router.register(r'reviews', ReviewViewSet, basename='review')

app_name = 'projects'

urlpatterns = [
    path('', include(router.urls)),
]