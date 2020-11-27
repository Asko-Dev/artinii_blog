from django.urls import path
from .views import PostListViewPublicUser, MoviesListView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostListViewUser
from . import views

urlpatterns = [
    path('', views.home, name='artinii-home'),
    path('user/<str:username>', PostListViewPublicUser.as_view(), name='user-posts-public'),
    path('blog', PostListView.as_view(), name='movie-blog'),
    path('submitted-movies/', MoviesListView.as_view(), name='movie-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('my-artinii/', PostListViewUser.as_view(),
         name='post-user', kwargs={'competition': None}),
    path('about/', views.about, name='blog-about'),
]
