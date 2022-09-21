from rest_framework import serializers
from music.models import Album, Artist, Song

class ArtistSerializer(serializers.ModelSerializer):
    music = serializers.PrimaryKeyRelatedField(many=True,queryset=Artist.objects.all())
    class Meta:
        model: Artist
        fields = [ 'id', 'firstname', 'artist']

class AlbumSerializer(serializers.ModelSerializer):
    #music = serializers.PrimaryKeyRelatedField(many=True, queryset=Album.objects.all())
    artist = ArtistSerializer()
    class Meta:
        model: Album
        fields = [ 'id', 'albumName', 'date_released', 'style', 'artist']
    
    def create(self, validated_data):
        return Album.objects.create(**validated_data)
    

class SongSerializer(serializers.ModelSerializer):
    #music = serializers.PrimaryKeyRelatedField(many=True, queryset=Song.objects.all())
    artist = ArtistSerializer()
    class Meta:
        model: Song
        fields = ['id', 'songName', 'albumName', 'date_released', 'style', 'artist']

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
    
