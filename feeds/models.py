from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Feeds(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	text=models.TextField()
	likes=models.IntegerField()
	image = models.ImageField(blank=True,null=True, upload_to='feed_pics')

	def __str__(self):
    	return f'{self.user.username} Profile'

    