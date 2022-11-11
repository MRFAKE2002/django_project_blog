from django import forms

from .models import Blog , PostComment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'text', 'status']


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['body', 'stars']

