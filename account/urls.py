from django.conf.urls import patterns, url

from account import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='account'),
    url(r'^login$', views.get_login, name='login'),
    url(r'^register$', views.register, name='register'),
)