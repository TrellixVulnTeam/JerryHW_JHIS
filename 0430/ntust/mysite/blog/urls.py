from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.post_page, name='new'),
    url(r'^edit/$', views.edit_page, name='edit'), 
    url(r'^view/$', views.view, name='view'),
    url(r'^save/$', views.save, name='save'), 
    url(r'^update/$', views.update, name='update'), 
    url(r'^delete/$', views.delete, name='delete'), 
]