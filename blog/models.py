from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(default="Type your text here", null=True)
    image = models.ImageField(upload_to='blog_pics', null=True)
    title2 = models.CharField(max_length=100, blank=True, null=True)
    content2 = models.TextField(default="Type your text here", null=True)
    image2 = models.ImageField(upload_to='blog_pics', null=True)
    title3 = models.CharField(max_length=100, null=True)
    content3 = models.TextField(default="Type your text here", null=True)
    content4 = models.TextField(default="Type your text here", null=True)
    link = models.URLField(default="www.hi.com", null=True)
    link2 = models.URLField(default="www.hi.com", null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
