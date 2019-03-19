from django.db import models

# to work with a model directly in admin panel register the model in /music/admin.py

# to access db api from shell write python manage.py shell
# from music.models import Album, Song
# s1 = Song(album=Album.objects.get(pk=3), file_type='mp3', song_title='Lets dance..')
# s1.save()
# album1.song_set.all() gives us all album 1 songs
# album1.song_set.count() gives us number of songs in album 1
# exit()

# whenever you make change in schema make migrations in terminal
# python manage.py makemigrations music
# python manage.py migrate
# run the server again

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.artist + ' - ' + self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    isFavourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

