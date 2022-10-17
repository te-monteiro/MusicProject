from rest_framework import serializers
from music.models import Album, Artist, Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "first_name", "last_name", "birthday", "age"]


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "album_name", "artist", "date_released", "style"]

    def to_representation(self, obj):
        self.fields["artist"] = ArtistSerializer()
        return super().to_representation(obj)


class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ["id", "song_name", "album_name", "date_released", "artist"]
