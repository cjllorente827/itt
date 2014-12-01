from django.conf.urls import patterns, url

"""
Url pattern matching convention distinguishes between page view requests and REST calls
Pageview request patterns MUST use GET and may not contain the word 'api'. They should dispatch to a method that
begins with 'view_'.

REST calls MUST be prefixed with 'api' and can use one of GET, POST, PUT, or DELETE which must be mapped to a method
that begins with 'read_', 'create_', 'update_', or 'delete_', respectively.
"""

#change this!!!
# from app_name import views

# urlpatterns = patterns('u',
#     url(r'^$', views.index, name='index'),
# )