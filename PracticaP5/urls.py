"""PracticaP5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from copy import name

from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from rest_framework.authtoken import views as authtoken_views

from Pentagram.views import comments, users, photos, like

urlpatterns = [
    url(r'^api/v1/login/$', authtoken_views.obtain_auth_token),
    url(r'^api/v1/photos/$', photos, name='photos'),
    url(r'^api/v1/users/$', users, name='users'),
    url(r'^api/photos/(?P<id_photo>[0-9]*)/like/$', like, name="like"),
    url(r'^api/photos/(?P<id_photo>[0-9]*)/comments/$', comments, name="comments"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/login', auth_views.login, {'template_name': 'login.html'}, name = "login"),
    url(r'^$', TemplateView.as_view(template_name = 'index.html'), name = "homepage"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
