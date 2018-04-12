from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^destroy/(?P<id>\d+)/confirm$', views.confirm_destroy),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
]