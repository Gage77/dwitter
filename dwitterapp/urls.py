from django.conf.urls import url

from . import views

urlpatterns = [
    # Index page
    url(r'^$', views.index, name='index'),
    # Account page
    url(r'account/(?P<account_username>[a-zA-Z0-9_.-]*)/$', views.account, name='account'),
    # Individual post
    url(r'(?P<post_id>[0-9]+)/$', views.post, name='post'),
    # Comments
    url(r'^(?P<post_id>[0-9]+)/comment/$', views.comment, name='comment'),
]
