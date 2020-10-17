from django.db import models

# Create your models here.
class MovieTable(models.Model):
	movie_name = models.CharField(max_length=50)
	release_date = models.DateField()
	hero_name = models.CharField(max_length=50)
	heroin_name = models.CharField(max_length=50)
	language = models.CharField(max_length=50)

