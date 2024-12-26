from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    bio = models.TextField()
    image = models.ImageField(upload_to='image/')
    website = models.URLField(null=True, blank=True)


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follower_users')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following_user')
    crated_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='post')
    image = models.ImageField(upload_to='image_post/')
    video = models.FileField(upload_to='video_post/')
    description = models.TextField()
    hashtag = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'post']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.TextField()
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'comment']


class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image_story/')
    video = models.FileField(upload_to='video_story/')
    created_at = models.DateTimeField(auto_now_add=True)


class Save(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class SaveItem(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    save = models.ForeignKey(Save, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
