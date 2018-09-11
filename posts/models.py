from django.urls import reverse
from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('posts:detail', args=[self.id])
