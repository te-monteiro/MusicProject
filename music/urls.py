from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from music import views


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'artist', views.ArtistViewSet,basename="artist")
router.register(r'album', views.AlbumViewSet,basename="album")
router.register(r'song', views.SongViewSet,basename="song")

urlpatterns = [
    path('', include(router.urls)),
]






"""
urlpatterns = ([
    #path('', views.api_root),
    path('artist-list/', views.ArtistList.as_view()),
    path('artist-details/<int:pk>/', views.ArtistDetails.as_view()),
    path('album-list/', views.AlbumList.as_view()),
    path('album-details/<int:pk>/', views.AlbumDetails.as_view()),
    path('song-list/', views.SongList.as_view()),    
    path('song-details/<int:pk>/', views.SongDetails.as_view()),
])
urlpatterns = format_suffix_patterns(urlpatterns)"""
