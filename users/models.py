from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	webiste=models.URLField(null=True)
	phone=models.CharField(max_length=10)
	dob=models.DateField()
	gender=models.CharField(max_length=10)
