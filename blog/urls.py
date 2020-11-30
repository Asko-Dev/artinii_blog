from django.urls import path
from .views import (
    PostListViewPublicUser,
    PostListView, PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostListViewUser
    )
from . import views

urlpatterns = [
    path('blog', PostListView.as_view(), name='movie-blog'),
    path('blog/user/<str:username>', PostListViewPublicUser.as_view(), name='user-posts-public'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('my-posts/', PostListViewUser.as_view(),
         name='post-user', kwargs={'competition': None}),
]
