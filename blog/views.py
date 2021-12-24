from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.htm'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.htm'