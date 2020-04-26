"""lectures_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

# FOR MEDIA
from django.conf.urls.static import static
from django.conf import settings

# FOR JWT
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),

    # USERES, SUB_PERSONES, CLASSES
    path("api/", include("users.urls")),
    path("api/", include("sub_persones.urls")),
    path("api/", include("classes.urls")),

    # REST
    path("rest/", include("rest_framework.urls")),
    path("rest-auth/", include('rest_auth.urls')),
    path("rest-auth/registration/", include('rest_auth.registration.urls')),

    # JWT
    path('token-auth/', obtain_jwt_token),
    path('token-refresh/', refresh_jwt_token),
    path('token-verify/', verify_jwt_token),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
