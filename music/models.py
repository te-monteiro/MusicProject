from django.db import models
import datetime


# Create your models here.
class Artist(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday=models.DateField(auto_now=False, null=True, blank=True)
    def age(self):
        return int((datetime.date.today() - self.birthday).days / 365.25  )
    age = age()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Album(models.Model):
    album_name = models.CharField(max_length=70)
    artist = models.CharField(max_length=50)
    date_released = models.DateField(default=None)
    style = models.CharField(max_length=50)

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, blank=True)
    song_name = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    date_released = models.DateField(default=None)

