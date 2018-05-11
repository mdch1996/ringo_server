from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ip/$', views.add_ip, name="ip"),
    url(r'^ring/$', views.add_ring, name="ring"),
    url(r'^sensor/$', views.add_sensor, name="sensor"),
]
