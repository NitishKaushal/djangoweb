"""seosite URL Configuration

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
import django
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from seo import views as seo_views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^post/(.*)$', seo_views.post),
    url(r"^$", seo_views.index),          # main page
    url(r'^about/', seo_views.aboutus),
    url(r'^admin/', admin.site.urls),
    url(r'^proposal/', seo_views.auditform, name='proposalinfo'),
    url(r'^seo/' , seo_views.seopage),
    url(r'^pay-per-click/' , seo_views.ppc),
    url(r'^social-media-marketting/' , seo_views.smo),
        url(r'^amazon-seo/' , seo_views.amazonseo),
      ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
