from django.urls import path
#from . import views
from .views import home, PostsView, PostDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', home, name='home'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('posts/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('posts/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
]
