# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from ch.models import Post

def hello(request):

	posts = Post.objects.all()

	return render(request, "threads.html", {"posts": posts})