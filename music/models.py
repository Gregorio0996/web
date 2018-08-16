from django.db import models
from django.urls import reverse


class Album(models.Model):
    artis = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    favorite_is = models.BooleanField(default=False)

    def get_absoulte_url(self):
        return reverse('music:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + '--' + self.artis


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    favorite_is = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
