"""Django_go URL Configuration

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
from Django_app_001.views.views_app_001 import index_go
from Django_app_001.views.app_001_login import app_001_login, app_001_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_go),

    # login/logout
    path('accounts/login/', app_001_login),
    path('accounts/logout/', app_001_logout),

    # app urls模块路径，app名字，APP的唯一namespace
    path('Django_app_001/', include(('Django_app_001.urls', 'Django_app_001'), namespace='Django_app_001')),
    path('Http_request/', include(('Http_request.urls', 'Http_request'), namespace='Http_request'))
]
