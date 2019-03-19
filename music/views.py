from django.http import Http404
from django.http import HttpResponse
from django.template import loader # needed for templates
from django.shortcuts import render, get_object_or_404 # used for shortcut of loading template
from .models import Album, Song

# long method of template
# def index(request):
#     all_albums = Album.objects.all()
#     template = loader.get_template('music/index.html')  # dont add templates to path because python itself looks in templates folder
#     context = {'all_albums': all_albums,} # make a dictionary to pass data to template
#     return HttpResponse(template.render(context, request))

def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums}) # render itself returns an http response

# long method for 404 error
# def detail(request, album_id):
#     try:
#         album = Album.objects.get(pk=album_id)
#     except Album.DoesNotExist:
#         raise Http404('Album does not exist')
#     return render(request, 'music/detail.html', {'album': album})

# shortcut for 404
def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {'album': album, 'error_message': 'Invalid song selected'})
    else:
        selected_song.isFavourite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})


