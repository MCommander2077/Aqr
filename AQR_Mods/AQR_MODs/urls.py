"""
URL configuration for AQR_MODs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.staticfiles.views import serve
from django.urls import re_path

from index.views import index_view as index
from index.views import info_view as info
from index.views import info_404 as info_404
from index.views import api as api

def return_static(request, path, insecure=True, **kwargs):
  return serve(request, path, insecure, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'), # 添加这行用来修复admin页面css404的原因
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('info/<id>/', info, name='info'),
    path('info/', info_404, name='info_404'),
    path('api/', api, name='api')
]
