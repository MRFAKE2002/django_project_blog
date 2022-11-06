from django.shortcuts import render
from django.views import generic 

from .models import Blog

class BlogListView(generic.ListView):
    # model = Blog
    queryset = Blog.objects.filter(status='pub').order_by('date_time_modified')
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    