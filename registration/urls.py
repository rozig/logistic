from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about-us/$', views.about, name='about'),
    url(r'^services/$', views.services, name='services'),
    url(r'^contact-us/$', views.contact, name='contact'),
    url(r'^delivery/$', views.delivery_detail, name='delivery_detail'),
]