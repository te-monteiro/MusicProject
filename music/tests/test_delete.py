from multiprocessing.spawn import old_main_modules
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

import datetime
from music.models import  Artist, Album



class TestDeleteArtistModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Teresa', password='test')
        self.client = APIClient()
        self.user.save()  

    def test_delete_artist_instance(self):
        artist = Artist.objects.create(
            first_name="John1",
            last_name="Lawrence",
            birthday = "1999-11-11",
            age = datetime.timedelta(days =1)
        )
        
        self.client.force_authenticate(self.user)
        
        request = self.client.delete('/artist/1', artist.pk, format='json')

        print(request)
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

class TestDeleteAlbumModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Teresa', password='test')
        self.client = APIClient()
        self.user.save()

    def test_delete_setView_album_instance(self):
        artist = Artist.objects.create(
            first_name="John1",
            last_name="Lawrence",
            birthday = "1999-11-11",
            age = datetime.timedelta(days =1)
        )
        self.client.force_authenticate(self.user)

        request = self.client.delete('/album/1', {'album_name': 'Chilling'}, format='json')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)


class TestDeleteSongModel(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='Teresa', password='test')
        self.client = APIClient()
        self.user.save()

    def test_delete_setView_song_instance(self):
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
        
        request = self.client.delete('/song/1', {'artist':artist.pk, 'album_name' : album.pk}, format='json')

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
