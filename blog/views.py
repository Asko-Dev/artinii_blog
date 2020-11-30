from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    base,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Post


def _context_data(self, view_type, **kwargs):
    article = Post.objects.filter(status="ACTIVE").order_by('?').first()
    context_data = super(view_type, self).get_context_data(**kwargs)
    context_data['main_title'] = article.main_title
    image = article.image
    context_data['image'] = image if image else article.image2
    context_data['slug'] = article.slug
    return context_data


class PostListView(ListView):
    model = Post
    template_name = 'blog/movie_blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        qs = Post.objects.filter(status="ACTIVE")
        tag = self.request.GET.get('tag')
        if tag:
            qs = Post.objects.filter(tag__icontains=tag)
        return qs

    def get_context_data(self, **kwargs):
        context_data = _context_data(self, PostListView, **kwargs)
        context_data['tag_dict'] = Post.objects.first().template_helper
        return context_data


class PostListViewPublicUser(ListView):
    model = Post
    template_name = 'blog/user_posts_public.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context_data = _context_data(self, PostListViewPublicUser, **kwargs)
        return context_data


class PostListViewUser(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_user.html'  # app/model/viewtype.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context_data = _context_data(self, PostListViewUser, **kwargs)
        return context_data


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context_data = _context_data(self, PostDetailView, **kwargs)
        return context_data


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = '__all__'
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'blog/post_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
