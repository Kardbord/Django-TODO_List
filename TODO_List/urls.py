from django.conf.urls import url

from . import views

app_name = 'TODO_List'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<todo_id>[0-9]+)/$', views.detail, name='detail'),
]