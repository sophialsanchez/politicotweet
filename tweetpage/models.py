from django.db import models

# Create your models here.
class Result(models.Model):
	title = models.CharField(max_length=100)
	img_src = models.CharField(max_length=100)
	description = models.TextField(max_length=10000)
	slug = models.SlugField(max_length=50)
	def __str__(self):
		return self.title