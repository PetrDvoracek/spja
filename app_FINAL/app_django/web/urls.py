from django.urls import path
from . import views


urlpatterns = [
    path('',views.web, name='web-home'),
    path('items', views.items, name='items'),
    path('band/<int:band_id>/', views.band, name='band'),
    path('album/<int:album_id>', views.album, name='album'),
    path('song/<int:song_id>', views.song, name='song'),
    path('new', views.new,name='new'),
    path('new/band/', views.get_band, name='get_band'),
    path('new/album/', views.get_album, name='get_album'),
    path('new/song/', views.get_song, name='get_song'),
    path('delete/song/<int:song_id>', views.song_delete, name='delete_song'),
    path('delete/album/<int:album_id>', views.album_delete, name='delete_album'),
    path('delete/band/<int:band_id>', views.band_delete, name='delete_band'),
    path('about/', views.about, name='about')

]

