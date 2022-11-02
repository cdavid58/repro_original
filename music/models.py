from django.utils.crypto import get_random_string
from django.db import models
from user.models import User

class Bar(models.Model):
	code = models.CharField(max_length = 10, unique=True, default = get_random_string(length=10))
	name = models.CharField(max_length = 40)
	lat = models.CharField( max_length=15)
	lon = models.CharField( max_length=15)
	block = models.BooleanField(default= False)

	def __str__(self):
		return self.name


class Music(models.Model):
	name = models.CharField(max_length = 100)
	artist = models.CharField(max_length = 100)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	bar = models.ForeignKey(Bar, on_delete = models.CASCADE)
	