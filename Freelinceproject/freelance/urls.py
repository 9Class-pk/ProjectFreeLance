"""
URL configuration for freelance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.i18n import i18n_patterns
from projects.views import RegisterView, LoginView, LogoutView

schema_view = get_schema_view(
    openapi.Info(
        title="Freelance Marketplace API",
        default_version='v1',
        description="API документация",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = i18n_patterns (
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('accounts/', include('allauth.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger.yaml', schema_view.without_ui(cache_timeout=0), name='schema-yaml'),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),
)

