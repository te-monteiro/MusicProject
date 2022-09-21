from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from music import views



urlpatterns = ([
    #path('', views.api_root),
    path('music/', views.ArtistDetails.as_view(), name='artist-details'),
    path('music/', views.AlbumDetails.as_view(), name='album-details'),
    path('music/', views.SongDetails.as_view(), name='song-details'),

])