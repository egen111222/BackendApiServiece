from django.conf import settings
from django.db import models

class Master(models.Model):
	name 			= models.CharField(max_length=40,null=False)
	experience  	= models.IntegerField()

	def __str__(self):
		return self.name
