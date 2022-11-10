from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _ # we use this function to translate our verbose_name
from django.contrib.auth import get_user_model
from django.utils import timezone


class Blog(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='post_user')
    title = models.CharField(_('Title'), max_length=50,)
    text = models.TextField(_('description'))
    status = models.CharField(_('Status'), choices=STATUS_CHOICES,  max_length=3)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    date_time_created = models.DateTimeField(_('date_time_created'), default=timezone.now)
    date_time_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.pk])


class PostComment(models.Model):
    POSTS_STARS = [
        ('1', _('very bad')),
        ('2', _('bad')),
        ('3', _('good')),
        ('4', _('very good')),
    ]
    
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(_('body'),)
    stars = models.CharField(_("stars"), choices=POSTS_STARS, max_length=10)
    
    datetime_created = models.DateTimeField(_('datetime_created'), default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)
