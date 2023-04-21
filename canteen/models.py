from distutils.command.upload import upload
from signal import default_int_handler
from tabnanny import verbose
from unicodedata import category

from django.db import models


class Category(models.Model):
	name = models.CharField(max_length= 100, db_index = True)
	slug = models.SlugField(max_length=100, unique=True)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name


class Food(models.Model):
	name = models.CharField(max_length= 100, db_index = True)
	slug = models.SlugField(max_length=100, unique=True)
	price = models.IntegerField()
	category = models.ForeignKey(Category, related_name='food', on_delete= models.CASCADE)
	updated = models.DateTimeField(auto_now = True)
	still_left = models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = 'foods'

	def __str__(self):
		return self.name

