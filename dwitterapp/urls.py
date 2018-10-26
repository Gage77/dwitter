from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from dwitterapp.views import postListView, postDetailView, postCreateView, postUpdateView, postRemoveView


urlpatterns = [
    # Index
    url(r'^$', postListView.as_view(), name='post_list'),
    # Posts
    url(r'^post/', include([
        url(r'^add/$', login_required(postCreateView.as_view()), name='post_add'),
        url(r'^(?P<pk>\d+)/', include([
            url(r'^$', postDetailView.as_view(), name='post_detail'),
            url(r'^edit/$', login_required(postUpdateView.as_view()), name='post_edit'),
            url(r'^remove/$', login_required(postRemoveView.as_view()), name='post_remove'),
        ]))
    ]))
]
