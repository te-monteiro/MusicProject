from multiprocessing.spawn import old_main_modules

from music.models import Artist, Album, Song

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

from django.contrib.auth.models import User
import datetime

class TestUpdateArtistModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Teresa', password='test')
        self.client = APIClient()
        self.user.save()

    def test_update_setView_artist_instance(self):
        artist = Artist.objects.create(
            first_name="John1",
            last_name="Lawrence",
            birthday = "1999-11-11",
            age = datetime.timedelta(days =1)
        )
        self.client.force_authenticate(self.user)

        request = self.client.put('/artist/1/', {'first_name': 'John1', 'last_name':'Lawrence', 'birthday':'1999-11-11', 'age':'07:00:00'}, format='json')

        print("AAAAAAA" , request.json())
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(Artist.objects.count(), 1)

class TestUpdateAlbumModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Teresa', password='test')
        self.client = APIClient()
        self.user.save()

    def test_update_setView_album_instance(self):
        artist = Artist.objects.create(
            first_name="John1",
            last_name="Lawrence",
            birthday = "1999-11-11",
            age = datetime.timedelta(days =1)
        )
        album = Album.objects.create(
            album_name = "testAlbum",
            artist = artist,
            date_released = "2020-11-20",
            style = "rock"
        )
        self.client.force_authenticate(self.user)

        request = self.client.put('/album/1', {'album_name': 'Chilling', 'artist':artist.pk, 'date_released':'2020-11-11', 'style':'Jazz'}, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)


class TestUpdateSongModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Teresa', password='test')
        self.client = APIClient()
        self.user.save()
        
    def test_update_setView_song_instance(self):
        self.client.force_authenticate(self.user)
        
        artist = Artist.objects.create(
            first_name="John1",
            last_name="Lawrence",
            birthday = "1999-11-11",
            age = datetime.timedelta(days =1)
        )
        
        album = Album.objects.create(
            album_name = "testAlbum",
            artist = artist,
            date_released = "2020-11-20",
            style = "rock"
        )
        song = Song.objects.create(
            artist = artist,
            song_name = "testSong",
            album_name = album,
            date_released = "2020-11-20"
        )
        self.client.force_authenticate(self.user)
        request = self.client.put('/song/1', {'artist':artist.get_full_name(),
            'song_name':'Vibing', 'album_name' : album.pk,      
            'date_released':'2020-11-20'}, format='json')

        self.assertEqual(request.status_code, status.HTTP_200_OK)
