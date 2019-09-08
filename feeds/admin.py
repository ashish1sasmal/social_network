from django.forms import Textarea
from django.contrib import admin
from django.db import models
# Register your models here.
from .models import Post
from ckeditor.fields import RichTextField

class PostAdmin(admin.ModelAdmin):
	formfield_overrides={
	RichTextField:{'widget':Textarea(attrs={'rows':4,'cols':60})}
	}
admin.site.register(Post,PostAdmin)