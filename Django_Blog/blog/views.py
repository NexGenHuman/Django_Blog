from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

class PostsView(ListView):
    model = Post
    template_name = 'posts.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = ['author', 'title', 'category', 'body', 'header_image', 'requires_permission', 'password']
