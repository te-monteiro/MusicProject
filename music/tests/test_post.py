from multiprocessing.spawn import old_main_modules
from django.test import TestCase

from music.models import  Artist

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
        #client = APIClient()
        #create an user 
        self.client.force_authenticate(self.user)
        request = self.client.post('/artist/', {'first_name': 'John1', 'last_name':'Lawrence', 'birthday':'1999-11-11', 'age':'06:00:00'}, format='json')

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(Artist.objects.count(), 1)

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
        #client = APIClient()
        self.client.force_authenticate(self.user)

        request = self.client.post('/album/', {'album_name': 'Chilling', 'artist': artist.pk, 'date_released':'2020-11-11', 'style':'Jazz'}, format='json')
        print("bbbbbbbbbbbbbbbb " , request.json())
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(Album.objects.count(), 1)

class TestCreateSongModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Teresa', password='test')
        self.client = APIClient()
        self.user.save()

    def test_create_setView_song_instance(self):
        #client = APIClient()
        
        #request_album = client.post('/album-list/', {'album_name': 'Chilling', 'artist':'John Lawrence', 'date_released':'2020-11-11', 'style':'Jazz'}, format='json')
        self.client.force_authenticate(self.user)

        request = self.client.post('/song-list/', {'artist':{'first_name': 'John1', 'last_name':'Lawrence', 'birthday':'1999-11-11', 'age':'06:00:00'},
            'song_name':'Vibing', 'album_name' : {'album_name':'Chilling', 'artist':'John Lawrence', 'date_released':'2020-11-20', 'style':'Jazz'},      
            'date_released':'2020-11-20'}, format='json')

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
      #  self.assertEqual(Song.objects.count(), 1)
