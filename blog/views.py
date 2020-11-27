from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from competition.models import AmateurCompetition

    # ukazka jak spojit dve app instance v jeden context
    # def home(request):
    #     context = {
    #         'posts': Post.objects.filter(),
    #         'submissions': AmateurCompetition.objects.filter()
    #     }
    #     return render(request, 'blog/home.html', context)



class PostListView(ListView):
    model = Post
    template_name = 'blog/movie_blog.html'  # app/model/viewtype.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostListViewPublicUser(ListView):
   model = Post
   template_name = 'blog/user_posts_public.html' #app/model/viewtype.html
   context_object_name = 'posts'
   paginate_by = 5

   def get_queryset(self):
       user = get_object_or_404(User, username=self.kwargs.get('username'))
       return Post.objects.filter(author=user).order_by('-date_posted')

def home(request):
    return render (request, 'blog/home.html', {'title': 'Artinii Home'})

class MoviesListView(ListView):
    model = AmateurCompetition
    template_name = 'blog/movie_list.html'  # app/model/viewtype.html
    context_object_name = 'movies'
    ordering = ['-date_posted']

class PostListViewUser(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_user.html'  # app/model/viewtype.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    # Mixin to update the context
    # https://docs.djangoproject.com/en/1.8/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.get_context_data
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update({
            'submissions': AmateurCompetition.objects.filter(user=self.request.user)
        })
        return context


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'title2', 'content2', 'image2', 'title3', 'content3', 'content4', 'link', 'link2']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image', 'title2', 'content2', 'image2', 'title3', 'content3', 'content4', 'link', 'link2']
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


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
