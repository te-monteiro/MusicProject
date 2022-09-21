from django.test import TestCase

from music.models import Artist
import datetime

class TestArtistModel(TestCase):
    def test_create_artist_instance(self):
        artist = Artist.objects.create(
            first_name="test",
            last_name="test",
            birthday = "1998-11-11 06:00Z",
            age = datetime.timedelta(days =1)
        )

        full_name = artist.get_full_name()
        self.assertEqual(full_name, "test test!")