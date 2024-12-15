from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name

class Painting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    creation_date = models.DateField()

    def __str__(self):
        return self.title

class Gallery(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    paintings = models.ManyToManyField(Painting)

    def __str__(self):
        return self.name
