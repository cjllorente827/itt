from django.conf.urls import patterns, url

from thread import views

urlpatterns = patterns('',
	url(r'^$', views.index),
	url(r'^(?P<thread_id>\d+)$',  views.method_dispatch(GET = views.read_thread)),
	url(r'^(?P<thread_id>\d+)/message$',  views.method_dispatch(POST = views.create_message)),
)