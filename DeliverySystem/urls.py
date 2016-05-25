"""DeliverySystem URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from registration import views as registration_views
from registration.forms import ContactForm

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'delivery', registration_views.DeliveryViewSet)

urlpatterns = [
    #Django-Jet URLs
	url(r'^jet/', include('jet.urls', 'jet')),
	url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    
    #Django default URLs
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'', include('registration.urls', namespace='registration')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^api/', include(router.urls)),

    #Django-AllAuth URLs
    url(r'^accounts/', include('allauth.urls')),

    #ContactForm URLs
    url(r'^contact-us/$', registration_views.contact_us, name='contact-us'),
    url(r'^thanks/$', registration_views.thanks, name='thanks'),
    
    #Report URLs
    url(r'^report_builder/', include('report_builder.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
