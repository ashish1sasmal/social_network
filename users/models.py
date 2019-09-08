from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	website=models.URLField(null=True)
	phone=models.CharField(max_length=10)
	dob=models.DateField()
	gender=models.CharField(max_length=10)
	bio=models.CharField(max_length=50)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')


	def __str__(self):
		return self.user.username

	def save(self):
		super().save()
		img=Image.open(self.image.path)
