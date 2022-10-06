from multiprocessing.spawn import old_main_modules
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

class TestDeleteArtistModel(APITestCase):
    def test_update_artist_instance(self):
        client = APIClient()

        request = client.delete('/artist/', {'first_name': 'John1', 'last_name':'Lawrence'}, format='json')

        print(request)
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

class TestDeleteAlbumModel(APITestCase):
    def test_create_setView_album_instance(self):
        client = APIClient()

        request = client.delete('/album/', {'album_name': 'Chilling'}, format='json')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)


class TestDeleteSongModel(APITestCase):
    def test_create_setView_song_instance(self):
        client = APIClient()
        
        request = client.delete('/song-list/', {'artist':{'first_name': 'John1', 'last_name':'Lawrence'}, 'album_name' : {'album_name':'Chilling'}}, format='json')

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
