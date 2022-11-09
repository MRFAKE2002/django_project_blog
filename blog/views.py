from django.shortcuts import render
from django.views import generic 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model

from .models import Blog
from .forms import BlogPostForm

class BlogListView(generic.ListView):
    # model = Blog
    queryset = Blog.objects.filter(status='pub').order_by('date_time_created')
    paginate_by = 3
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

# for make a new book we need user login and for class we must use method " LoginRequiredMixin " mixin class
class BlogDetailView(LoginRequiredMixin, generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'


# for make a new book we need user login and for class we must use method " LoginRequiredMixin " mixin class
class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    form_class = BlogPostForm
    template_name = 'blog/blog_create.html'


# for make a new book we need user login and for class we must use method " LoginRequiredMixin " mixin class
# for change or delete a book we need user permission and we must use method " UserPassesTestMixin " from mixin class and we must fill method " test_func "
class BlogUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Blog
    form_class = BlogPostForm
    template_name = 'blog/blog_update.html'
    
    # def test_func(self):
    #     # return the book that we are updating
    #     obj = self.get_object()
    #     # self.request.user is the user who is login
    #     return obj.post_user == self.request.user



# for make a new book we need user login and for class we must use method " LoginRequiredMixin " mixin class
# for change or delete a book we need user permission and we must use method " UserPassesTestMixin " from mixin class and we must fill method " test_func "
class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog_list')
    
    def test_func(self):
        # return the book that we are updating
        obj = self.get_object()
        # self.request.user is the user who is login
        return obj.post_user == self.request.user

