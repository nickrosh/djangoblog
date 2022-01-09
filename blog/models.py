from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # on_delete=models.CASCADE means that if the tied Object (User) is deleted,
    # then all posts connected with that user will be deleted too

    # auto_now=True updates to current time at any update
    # last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # the post redirects to 
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    class Meta:
        ordering = ('date_posted',)

    def __str__(self):
        return f'Comment from {self.author.username} on {self.date_posted}'

    
