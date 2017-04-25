from django.conf.urls import url

from . import views

app_name = 'TODO_List'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.edit, { 'template_name' : 'TODO_List/new.html'}, name='new'),
    url(r'^edit/(?P<todo_id>[0-9]+)$', views.edit, name='edit'),
    url(r'^(?P<todo_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<todo_id>[0-9]+)/$', views.detail, name='detail'),
]