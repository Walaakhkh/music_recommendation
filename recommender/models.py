from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()

class UserSongInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=10, choices=[('listen', 'Listen'), ('like', 'Like'), ('skip', 'Skip')])
    timestamp = models.DateTimeField(auto_now_add=True)
