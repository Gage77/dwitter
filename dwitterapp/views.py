# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import arrow
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post


class postListView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 10

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


class postRemoveView(DeleteView):
    model = Post
    template_name = 'post_remove.html'
    success_url = reverse_lazy('post_list')
