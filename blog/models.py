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
