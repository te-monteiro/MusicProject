from multiprocessing.spawn import old_main_modules
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

from django.contrib.auth.models import User
import datetime

from music.models import  Artist, Album



class TestGetArtistModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Teresa', password='test')
        self.client = APIClient()
        self.user.save()

    def test_update_artist_instance(self):
        artist = Artist.objects.create(
            first_name="John1",
            last_name="Lawrence",
            birthday = "1999-11-11",
            age = datetime.timedelta(days =1)
        )
        self.client.force_authenticate(self.user)

        request = self.client.get('/artist/', {'first_name': 'John1', 'last_name':'Lawrence'}, format='json')

        self.assertEqual(request.status_code, status.HTTP_200_OK)

class TestGetAlbumModel(APITestCase):
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
        album = Album.objects.create(
            album_name = "testAlbum",
            artist = artist,
            date_released = "2020-11-20",
            style = "rock"
        )
        self.client.force_authenticate(self.user)

        request = self.client.get('/album/', {'album_name': 'Chilling'}, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)


class TestGetSongModel(APITestCase):
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

        request = self.client.get('/song/', {'artist': artist.pk, 'album_name' : {'album_name':'Chilling'}}, format='json')

        self.assertEqual(request.status_code, status.HTTP_200_OK)
