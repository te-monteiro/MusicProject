from multiprocessing.spawn import old_main_modules
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

from django.contrib.auth.models import User


class TestGetArtistModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Teresa', password='test')
        self.client = APIClient()
        self.user.save()

    def test_update_artist_instance(self):
        #artist id 
        self.client.force_authenticate(self.user)

        request = self.client.get('/artist/', {'first_name': 'John1', 'last_name':'Lawrence'}, format='json')

        print(request)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

class TestGetAlbumModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Teresa', password='test')
        self.client = APIClient()
        self.user.save()

    def test_create_setView_album_instance(self):
        self.client.force_authenticate(self.user)

        request = self.client.get('/album/', {'album_name': 'Chilling'}, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)


class TestGetSongModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Teresa', password='test')
        self.client = APIClient()
        self.user.save()

    def test_create_setView_song_instance(self):
        self.client.force_authenticate(self.user)

        
        #request_album = client.post('/album-list/', {'album_name': 'Chilling', 'artist':'John Lawrence', 'date_released':'2020-11-11', 'style':'Jazz'}, format='json')

        request = self.client.get('/song-list/', {'artist':{'first_name': 'John1', 'last_name':'Lawrence'}, 'album_name' : {'album_name':'Chilling'}}, format='json')

        self.assertEqual(request.status_code, status.HTTP_200_OK)
