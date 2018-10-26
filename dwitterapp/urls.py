from django.conf.urls import url, include

from dwitterapp.views import postListView, postDetailView, postCreateView, postUpdateView


urlpatterns = [
    url(r'^$', postListView.as_view(), name='post_list'),
    url(r'^post/', include([
        url(r'^add/$', postCreateView.as_view(), name='post_add'),
        url(r'^(?P<pk>\d+)/', include([
            url(r'^$', postDetailView.as_view(), name='post_detail'),
            url(r'^edit/$', postUpdateView.as_view(), name='post_edit'),
        ]))
    ]))
]
