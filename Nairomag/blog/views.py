from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('blog')


class BlogView(ListView):
    model= Post
    context_object_name = 'posts'
    template_name = 'blog/blog_list.html'


class PostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post.html'


class CreatePost(LoginRequiredMixin, CreateView):
    model =Post
    fields = ['title','brief','image','description']
    success_url = reverse_lazy('blog')
    template_name = 'blog/add.html'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(CreatePost, self).form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','brief','image','description']
    success_url = reverse_lazy('blog')


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('blog')
