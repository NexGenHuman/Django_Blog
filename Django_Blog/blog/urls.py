from django.urls import path
from .views import home, posts

urlpatterns = [
    path('', home, name='home'),
    path('posts/', posts.as_view(), name='posts')
]