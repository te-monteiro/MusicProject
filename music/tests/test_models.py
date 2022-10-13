#from multiprocessing.spawn import old_main_modules
from django.test import TestCase
import unittest


from music.models import  Artist, Album, Song
import datetime

class TestArtistModel(TestCase):
    def test_create_artist_instance(self):
        artist = Artist.objects.create(
            first_name="test",
            last_name="test",
            birthday = "1998-11-11",
            age = datetime.timedelta(days =1)
        )

        full_name = artist.get_full_name()
        self.assertEqual(full_name, "test test")

class TestAlbumModel(TestCase):
    def test_create_album_instance(self):
        album = Album.objects.create(
            album_name = "testAlbum",
            artist = "test",
            date_released = "2020-11-20",
            style = "rock"
        )

        album_name = album.get_album()
        self.assertEqual(album_name, "testAlbum - test")
        

class TestSongModel(TestCase):
     def test_create_song_instance(self):
        artist = Artist.objects.create(
            first_name="test",
            last_name="test",
            birthday = "1998-11-11",
            age = datetime.timedelta(days =1)
        )
        album = Album.objects.create(
            album_name = "testAlbum",
            artist = "test test",
            date_released = "2020-11-20",
            style = "rock"
        )
        song = Song.objects.create(
            artist = artist,
            song_name = "testSong",
            album_name = album,
            date_released = "2020-11-20"
        )
        
        self.assertEqual(song.artist.get_full_name(), "test test")

        self.assertEqual(song.album_name.get_album(), "testAlbum - test test")

        song_name = song.get_song()
        self.assertEqual(song_name, "testSong")

class TestDeleteAlbum(TestCase):
    def test_delete_album(self):
        artist = Artist.objects.create(
            first_name="John",
            last_name="Lawrence",
            birthday = "1998-11-11",
            age = datetime.timedelta(days =1)
        )
        album = Album.objects.create(
            album_name = "Chilling",
            artist = "John Lawrence",
            date_released = "2020-11-20",
            style = "Jazz"
        )
        song = Song.objects.create(
            artist = artist,
            song_name = "Vibing",
            album_name = album,      
            date_released = "2020-11-20"
        )

        self.assertEqual(song.artist.get_full_name(), "John Lawrence")

        self.assertEqual(song.album_name.get_album(), "Chilling - John Lawrence")

        self.assertEqual(song.get_song(), "Vibing")

        album.delete()
        #check this better
        #print("ALBUM ", song.album.get_album())
        #print("SONG " , Song.objects.get()) #  song.get_song()
