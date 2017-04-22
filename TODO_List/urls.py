from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<todo_id>[0-9]+)/$', views.detail, name='detail'),
]