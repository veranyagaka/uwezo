from django.db import models

# Create your models here.

## maps, discussions and forums
# voting perhaps ?
# email config
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(max_length=280)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # a bit buggy for now

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    @property
    def is_edited(self):
        return self.created_at == self.updated_at

    def __str__(self):
        return f'Post by {self.user.username}'

# Like model for users liking posts
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} liked post {self.post.id}'

# Comment model for users commenting on posts
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=500)  # Adjust as needed for comment length
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on post {self.post.id}'

# Relationship model for followers and following
class Relationship(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    followed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensure that a user can't follow the same user multiple times
        unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.follower.username} follows {self.following.username}'
class IncidentReport(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date_reported = models.DateTimeField(auto_now_add=True)
