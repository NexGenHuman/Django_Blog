from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, EditPostForm, CommentForm, UpdateCommentForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import json


# Create your views here.

def home(request):
    return render(request, 'home.html')

class PostsView(ListView):
    model = Post
    template_name = 'posts.html'


def PostDetailView(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            print('This is from form')
            form.instance.author = request.user
            form.instance.post = post
            form.save()
            return redirect('post-detail', pk=post.pk)
    
    context = {
        'post': post,
        'form': form
    }
    
    if 'post_cookie_' + str(post.pk) in request.COOKIES:
        return render(request, 'post-detail.html', context)
    
    if(post.requires_permission):
        json_data = json.loads(request.read().decode('utf-8'))
        password = json_data['password']
        print(password)
        
        if(post.password != password):
            print('Password is incorrect')
            return JsonResponse({'error': 'Password is incorrect'}, status=400)
    
    return render(request, 'post-detail.html', context)


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
    
class UpdateCommentView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Comment
    form_class = UpdateCommentForm
    template_name = 'update_comment.html'
    
    def get_success_url(self):
        comment = self.get_object()
        post_url = comment.post.get_absolute_url()
        return post_url
    #fields = ['text']

def DeleteCommentView(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.user == comment.author:
        post_id = comment.post.id
        comment.delete()
        return redirect('post-detail', post_id)