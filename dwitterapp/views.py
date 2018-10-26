# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import arrow
from django.views.generic import DetailView, CreateView, ListView, UpdateView

from .forms import PostForm
from .models import Post


# Create your views here.
class postListView(ListView):
    model = Post
    template_name = 'index.html'

    def get_queryset(self):
        qs = super(postListView, self).get_queryset()
        qs.filter(published_date__lte=arrow.now().datetime)
        return qs


class postDetailView(DetailView):
    model = Post
    template_name = 'post.html'


class postCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'


class postUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'
