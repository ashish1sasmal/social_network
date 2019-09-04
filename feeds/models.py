from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image

# Create your models here.

class Post(models.Model):
	text=models.TextField()
	image = models.ImageField(default='default.jpg', upload_to='feeds_pics')
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.author.username

	def save(self):
		super().save()
		img=Image.open(self.image.path)

	def get_absolute_url(self):
		return reverse('home')