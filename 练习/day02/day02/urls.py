"""day02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app01 import views #一般views是需要建立单独文件夹，这样区别不同的视图文件

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/',views.index ),   #index为函数名
    url(r'^login/',views.login ),   #index为函数名
    url(r'^login_submit/',views.login_submit ),   #index为函数名
]
