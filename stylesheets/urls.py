from django.conf.urls import patterns, url

from stylesheets import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)