from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	webiste=models.URLField(null=True)
	phone=models.CharField(max_length=10)
	dob=models.DateField()
	gender=models.CharField(max_length=10)
	# image = models.ImageField(blank=True,null=True, upload_to='profile_pics')


	def __str__(self):
		return self.user.username

	# def save(self):
	# 	super().save()
	# 	img=Image.open(self.image.path)
