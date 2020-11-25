from django.db import models

# Create your models here.
class MoviesData(models.Model):
    Rank = models.IntegerField()
    Title = models.CharField(max_length=100)
    Rating = models.FloatField()
    Metascore = models.IntegerField()
    Duration = models.IntegerField()
    Year = models.IntegerField()
    Category = models.CharField(max_length=100)
    Gross = models.IntegerField()
    Votes_number = models.IntegerField()
    Image = models.CharField(max_length=100)
