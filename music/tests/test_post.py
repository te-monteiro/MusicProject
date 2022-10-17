from multiprocessing.spawn import old_main_modules

from music.models import  Artist, Album

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

from django.contrib.auth.models import User
import datetime


class TestCreateArtistModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Teresa', password='test')
        self.client = APIClient()
        self.user.save()

    def test_create_setView_artist_instance(self):
        
        self.client.force_authenticate(self.user)
        request = self.client.post('/artist/', {'first_name': 'John1', 'last_name':'Lawrence', 'birthday':'1999-11-11', 'age':'06:00:00'}, format='json')

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

class TestCreateAlbumModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Teresa', password='test')
        self.client = APIClient()
        self.user.save()

    def test_create_setView_album_instance(self):
        artist = Artist.objects.create(
            first_name="John1",
            last_name="Lawrence",
            birthday = "1999-11-11",
            age = datetime.timedelta(days =1)
        )
        self.client.force_authenticate(self.user)

        request = self.client.post('/album/', {'album_name': 'Chilling', 'artist': artist.pk, 'date_released':'2020-11-11', 'style':'Jazz'}, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

class TestCreateSongModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Teresa', password='test')
        self.client = APIClient()
        self.user.save()

    def test_create_setView_song_instance(self):
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
        request = self.client.post('/song/', {'artist':artist.get_full_name(),
            'song_name':'Vibing', 'album_name' : album.pk,      
            'date_released':'2020-11-20'}, format='json')

        print("bbbbbbbbbbbbbbbb " , request.json())

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
