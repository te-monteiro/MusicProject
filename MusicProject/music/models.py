from tkinter import CASCADE
from django.db import models

# Create your models here.
class Artist(models.Model):
    # class Meta:
    #     ordering = ['created']
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateTimeField(default=None)
    age = models.DurationField(default=None)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Album(models.Model):
    albumName = models.CharField(max_length=70)
    artist = models.CharField(max_length=50)
    date_released = models.DateField(default=None)
    style = models.CharField(max_length=50)

class Song(models.Model):
    artist = models.CharField(max_length=50)
    songName = models.CharField(max_length=50)
    albumName = models.ForeignKey(Album, on_delete=models.CASCADE)
    date_released = models.DateField(default=None)

