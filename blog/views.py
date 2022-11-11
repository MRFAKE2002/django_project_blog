from django.shortcuts import get_object_or_404
from django.views import generic 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model

from .models import Blog , PostComment
from .forms import BlogPostForm , PostCommentForm

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
    
    # For show our PostCommentForm in product_detail in class we must overwrite a method to send our comment_form as a context
    # We use get_context_data for add or change anything in our code 
    # This method in django by default just get Product and comment from our model
    def get_context_data(self, **kwargs):
        # This code is default in django for get Product and Comment form model
        context = super().get_context_data(**kwargs)
        # We use this code to add PostCommentForm in the context and use it in our product_detail
        context['comment_form'] = PostCommentForm()
        return context


class PostCommentCreateView(generic.CreateView):
    model = PostComment
    form_class = PostCommentForm
    
    # Now for add author of comment in database we must overwrite this method 
    def form_valid(self, form):
        # get the comment body and stars from user request by CommentForm but we don't want to save it in database
        comment_model = form.save(commit=False)
        # get the comment user from the user that login
        comment_model.author = self.request.user

        # For get post of PostComment model we must get the post_id from the url that we get " post.id " by  POST request that user send comment
        post_id = int(self.kwargs['post_id'])
        post_page = get_object_or_404(Blog, pk=post_id)
        comment_model.post = post_page
        
        return super().form_valid(form)


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
    
    def test_func(self):
        # return the book that we are updating
        obj = self.get_object()
        # self.request.user is the user who is login
        return obj.post_user == self.request.user



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


