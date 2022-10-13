from rest_framework import serializers
from music.models import Album, Artist, Song

class ArtistSerializer(serializers.ModelSerializer):
    #music = serializers.PrimaryKeyRelatedField(many=True, queryset=Artist.objects.all())
    #artist = serializers.ReadOnlyField(source='artist.get_full_name()')

    class Meta:
        model= Artist
        fields = [ 'id', 'first_name', 'last_name', 'birthday', 'age']
        
    def create(self, validated_data):
        return Artist.objects.create(**validated_data)

class AlbumSerializer(serializers.ModelSerializer):
    #music = serializers.PrimaryKeyRelatedField(many=True, queryset=Album.objects.all())
    artist = ArtistSerializer()
    class Meta:
        model= Album
        fields = [ 'id', 'album_name', 'artist', 'date_released', 'style']
    
    def create(self, validated_data):
        return Album.objects.create(**validated_data)
    

class SongSerializer(serializers.ModelSerializer):
    #music = serializers.PrimaryKeyRelatedField(many=True, queryset=Song.objects.all())
    artist = ArtistSerializer()
    class Meta:
        model= Song
        fields = ['id', 'song_name', 'album_name', 'date_released', 'artist']

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
    
