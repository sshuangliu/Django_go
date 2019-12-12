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
from django.urls import path
from Django_app_001.views.views_app_001 import device_add, device_select, device_del, device_update, chartjs_from_django, chartjs_from_ajax, echarts_from_django, echarts_from_ajax, index_go
from Django_app_001.views.ajax_json import chartjs_ajax_json
from Django_app_001.views.app_001_login import app_001_login, app_001_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_go),
    path('device_add', device_add),
    path('device_select', device_select),
    path('device_del/<int:device_id>', device_del),
    path('device_update/<int:device_id>', device_update),
    path('chartjs_from_django', chartjs_from_django),
    path('chartjs_from_ajax', chartjs_from_ajax),
    path('chartjs_from_ajax/<str:chart_type>', chartjs_ajax_json),  # json_rpc
    path('echarts_from_django', echarts_from_django),
    path('echarts_from_ajax', echarts_from_ajax),

    # login/logout
    path('accounts/login/', app_001_login),
    path('accounts/logout/', app_001_logout),
]
