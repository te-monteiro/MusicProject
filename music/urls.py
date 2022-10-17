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
