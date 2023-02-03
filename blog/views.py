from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'postlist'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'body']

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_entry.html'
    fields = ['title', 'author', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
