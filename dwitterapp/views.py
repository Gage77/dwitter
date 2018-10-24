# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.utils import timezone

from .models import Post, Comment

from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = { 'latest_post_list': posts }
    return render(request, 'dwitterapp/index.html', context)


def post(request, post_id):
    thisPost = get_object_or_404(Post, pk=post_id)
    return render(request, 'dwitterapp/post.html', {'post': thisPost})


def comment(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    try:
        new_comment = p.comment_set.get(pk=request.POST['comment'])
    except (KeyError, Comment.DoesNotExist):
        # Redisplay the post
        return render(request, 'dwitterapp/post.html', {
            'post': p,
            'error_message': "Unable to comment on post"
        })
    else:
        new_comment.text = request.POST().get("new_comment")
        new_comment.save()
        return render(request, 'dwitterapp/post.html', {'post': p})


def account(request, account_username):
    return HttpResponse("You're looking at account %s." % account_username)


