from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Profile
from .forms import PostForm, ProfilePageForm, EditPostForm, CommentForm, UpdateCommentForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import json


# Create your views here.
class CreateProfilePage(CreateView):
    model = Profile
    template_name = 'create_profile_page.html'
    form_class = ProfilePageForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'edit_profile_page.html'
    success_url = reverse_lazy('home')
    form_class = ProfilePageForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'user_profile.html'

    def get_context_data(self, *args, **kwargs):
        #users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

def home(request):
    return render(request, 'home.html')

def PostsView(request):
    posts = Post.objects.all()
    
    if request.method == 'POST':
        search = request.POST['search']
        posts = Post.objects.filter(title__contains=search)
    
    context = {
        'object_list' : posts
    }
    
    return render(request, 'posts.html', context)


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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Post
    form_class = EditPostForm
    template_name = 'update_post.html'
    #fields = ['title', 'body']

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


class DeletePostView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('posts')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset
    
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