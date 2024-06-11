from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import PostForm
from .models import Post
from .filters import PostFilter


class PostList(ListView):
    model = Post
    ordering = 'title_post'
    template_name = 'post.html'
    context_object_name = 'post'
    order_by = '- time_in'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    ordering = 'title_post'
    template_name = 'post_search.html'
    context_object_name = 'post'
    order_by = '- time_in'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
