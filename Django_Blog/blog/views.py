from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, EditPostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def home(request):
    return render(request, 'home.html')

class PostsView(ListView):
    model = Post
    template_name = 'posts.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'


class AddPostView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = ['author', 'title', 'category', 'body', 'header_image', 'requires_permission', 'password']


class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Post
    form_class = EditPostForm
    template_name = 'update_post.html'
    #fields = ['title', 'body']


class DeletePostView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('posts')

def DeleteCommentView(request, pk):
    comment = Comment.objects.get(pk=pk)
    post_id = comment.post.id
    comment.delete()
    return redirect('post-detail', post_id)