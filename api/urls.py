from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ip/$', views.add_ip, name="ip"),
    url(r'^ring/$', views.add_ring, name="ring"),
    # url(r'^open/$', views.add_open, name="open"),
]
