from django.shortcuts import render
import music

from music.models import Album, Artist, Song
from music.serializers import ArtistSerializer, AlbumSerializer, SongSerializer

from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post', 'put', 'delete'], renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        artist = self.get_object()
        return Response(artist.highlighted)

    def perform_create(self, serializer):
        serializer.save()


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post', 'put', 'delete'], renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        album = self.get_object()
        return Response(album.highlighted)


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True,methods=['post', 'put', 'delete'], renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        song = self.get_object()
        return Response(song.highlighted)

    def perform_create(self, serializer):
        serializer.save()
