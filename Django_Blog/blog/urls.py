from django.urls import path
from .views import home, posts,  postDetail

urlpatterns = [
    path('', home, name='home'),
    path('posts/', posts.as_view(), name='posts'),
    path('posts/<int:pk>/', postDetail.as_view(), name='post-detail')
]