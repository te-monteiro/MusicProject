from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from music import views



urlpatterns = ([
    #path('', views.api_root),
    path('artist-list/', views.ArtistList.as_view()),
    path('artist-details/<int:pk>/', views.ArtistDetails.as_view()),
    path('album-list/', views.AlbumList.as_view()),
    path('album-details/<int:pk>/', views.AlbumDetails.as_view()),
    path('song-list/', views.SongList.as_view()),    
    path('song-details/<int:pk>/', views.SongDetails.as_view()),
])