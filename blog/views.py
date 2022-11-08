from django.shortcuts import render
from django.views import generic 
from django.urls import reverse_lazy

from .models import Blog
from .forms import BlogPostForm

class BlogListView(generic.ListView):
    # model = Blog
    queryset = Blog.objects.filter(status='pub').order_by('date_time_modified')
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'


class BlogCreateView(generic.CreateView):
    model = Blog
    form_class = BlogPostForm
    template_name = 'blog/blog_create.html'


class BlogUpdateView(generic.UpdateView):
    model = Blog
    form_class = BlogPostForm
    template_name = 'blog/blog_create.html'
    

class BlogDeleteView(generic.DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog_list')
    

