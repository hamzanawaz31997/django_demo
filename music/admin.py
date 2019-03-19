from django.contrib import admin
from .models import Album, Song


admin.site.register(Album)  #register a model in the admin panel for editing
admin.site.register(Song)