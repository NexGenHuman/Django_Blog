from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.

def home(request):
    return render(request, 'home.html')

class posts(ListView):
    model = Post
    template_name = 'posts.html'
    
class postDetail(DetailView):
    model = Post
    template_name = 'post-detail.html'
