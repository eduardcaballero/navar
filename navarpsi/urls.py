"""navarpsi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.urls import path, include
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django.views.generic.base import TemplateView
from navar import views as core_views

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url('', include('navar.urls')),
#    url(r'^home/', include('navar.urls')),
   url(r'^home/', TemplateView.as_view(template_name='usuario/home.html'), name='home'),
   url(r'^accounts/', include('django.contrib.auth.urls'),name='login'),
   url(r'^registrar/$', core_views.create_usuario, name='registrar'),
#    url(r'^accounts/login/$', views.login, name='login'),
# path('accounts/', include('django.contrib.auth.urls')),
]