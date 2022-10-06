from multiprocessing.spawn import old_main_modules

from music.models import  Artist

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

class TestUpdateArtistModel(APITestCase):
    def test_update_artist_instance(self):
        client = APIClient()

        request = client.put('/artist/', {'first_name': 'John1', 'last_name':'Lawrence', 'birthday':'1999-11-11', 'age':'06:00:00'}, format='json')

        print(request)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(Artist.objects.count(), 1)

class TestUpdateAlbumModel(APITestCase):
    def test_update_setView_album_instance(self):
        client = APIClient()

        request = client.put('/album/', {'album_name': 'Chilling', 'artist':'John1 Lawrence', 'date_released':'2020-11-11', 'style':'Jazz'}, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        #self.assertEqual(Album.objects.count(), 1)


class TestUpdateSongModel(APITestCase):
    def test_update_setView_song_instance(self):
        client = APIClient()
        
        #request_album = client.post('/album-list/', {'album_name': 'Chilling', 'artist':'John Lawrence', 'date_released':'2020-11-11', 'style':'Jazz'}, format='json')

        request = client.put('/song-list/', {'artist':{'first_name': 'John1', 'last_name':'Lawrence', 'birthday':'1999-11-11', 'age':'06:00:00'},
            'song_name':'Vibing', 'album_name' : {'album_name':'Chilling', 'artist':'John Lawrence', 'date_released':'2020-11-20', 'style':'Jazz'},      
            'date_released':'2020-11-20'}, format='json')

        self.assertEqual(request.status_code, status.HTTP_200_OK)
      #  self.assertEqual(Song.objects.count(), 1)