from django.db import models

class User(models.Model):
	number_phone = models.CharField(max_length=15)
	lat = models.CharField(max_length = 15)
	lon = models.CharField(max_length = 15)
	count_music = models.IntegerField(default = 5)
	penalizacion = models.IntegerField(default = 0)

	