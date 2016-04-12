from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^delivery/(?P<pk>\d+)/$', views.delivery_detail, name='delivery_detail'),
]