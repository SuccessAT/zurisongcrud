from django.db import models
from datetime import datetime
# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name

class Song(models.Model):
    title = models.CharField(max_length=400)
    date_released = models.DateTimeField(default=datetime.today)
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.song_id.title