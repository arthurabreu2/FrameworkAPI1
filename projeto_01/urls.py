"""projeto_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from frameworkapi.api.viewsets import JsonPlaceholderViewset


router = routers.DefaultRouter()
router.register('jsonplaceholder.typicode.com/todos', JsonPlaceholderViewset)


admin.site.site_header = "FrameworkAPI Desafio"
admin.site.site_title = "FrameworkAPI Desafio"
admin.site.index_title = "FrameworkAPI"


urlpatterns = [
    path('api', include(router.urls)),
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
