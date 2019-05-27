from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=150)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	location = models.CharField(max_length=100)
	salary = models.CharField(max_length=20)
	duration = models.CharField(max_length=15)
	date_posted = models.DateTimeField(default=timezone.now)
	contact = models.CharField(max_length=100)
	reference = models.CharField(max_length=25)
	description = models.TextField()

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	comment = models.CharField(max_length=290)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


	def __str__(self):
		return self.comment
	

	def get_absolute_url(self):
		return reverse('job-home')