from os import path

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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
    template_name = 'post_search.html'
    context_object_name = 'post'
    order_by = '- time_in'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        if self.request.GET:
            return self.filterset.qs
        return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if path == 'news/create/':
            post.type_text = "NEWS"
        if path == 'article/create/':
            post.type_text = "ARTI"
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if path == 'news/<int:pk>/edit':
            post.type_text = "NEWS"
        if path == 'article/<int:pk>/edit':
            post.type_text = "ARTI"
        return super().form_valid(form)


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_delete')

    def form_valid(self, form):
        post = form.save(commit=False)
        if path == 'news/<int:pk>/delete':
            post.type_text = "NEWS"
        if path == 'article/<int:pk>/delete':
            post.type_text = "ARTI"
        return super().form_valid(form)