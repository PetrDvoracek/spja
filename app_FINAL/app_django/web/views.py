from django.shortcuts import render,redirect,get_object_or_404
from .models import Band,Album,Song
from .forms import BandForm,AlbumForm,SongForm
# Create your views here.

#def get_band(request):
#    if request.method =='POST':
#        form = BandForm(request.POST)
#        if form.is_valid():
#            return HttpResponseRedirect('/thanks/')
#    else:
#        form = BandForm()
#    return render(request, 'web/new_band.html', {'form':form})


def song_delete(request, song_id):
    song = Song.objects.filter(id=song_id)
    song.delete()
    return web(request)

def album_delete(request, album_id):
    album = Album.objects.filter(id=album_id)
    album.delete()
    return web(request)

def band_delete(request, band_id):
    band = Band.objects.filter(id=band_id)
    band.delete()
    return web(request)


def get_band(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save(commit=False)
            band.save()
            #return redirect('/web/band', pk=band.pk)
    else:
        form = BandForm()
    return render(request, 'web/new_band.html', {'form': form})

def get_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            #return redirect('/web/band', pk=band.pk)
    else:
        form = AlbumForm()
    return render(request, 'web/new_album.html', {'form': form})

def get_song(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.save()
            #return redirect('/web/band', pk=band.pk)
    else:
        form = SongForm()
    return render(request, 'web/new_song.html', {'form': form})


def web(request):
    context = {
        'bands': Band.objects.all(),
        'albums' : Album.objects.all(),
        'songs' : Song.objects.all(),
        'title':'main page',
    }
    return render(request, 'web/web.html', context)


def items(request):
    return render(request, 'web/items.html')

def band(request, band_id):
    band = Band.objects.filter(id=band_id).first()
    albums = Album.objects.filter(band=band)
    songs = [x.song_set.all() for x in albums]
    songs = merge_query(songs)

    context = {
        'band': band,
        'albums': albums,
        'songs': songs,
    }
    return render(request, 'web/band.html',context)




def album(request, album_id):
    album = Album.objects.filter(id=album_id).first()
    songs = Song.objects.filter(album=album)
    context = {
        'album':album,
        'songs':songs,
    }
    return render(request, 'web/album.html', context)

def song(request, song_id):
    song = Song.objects.filter(id=song_id).first()
    return render(request, 'web/song.html', {'song':song})

def new(request):
    return render(request, 'web/new.html')

def about(request):
    return render(request, 'web/about.html')

def merge_query(ar):
    if len(ar) ==0:
        return [ar]
    while len(ar)>1:
        tmp=ar[0] | ar[1]
        ar[0]=tmp
        ar.pop(1)
        return ar
