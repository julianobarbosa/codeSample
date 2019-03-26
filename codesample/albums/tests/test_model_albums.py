from django.test import TestCase
from codesample.albums.models import Artista

class ArtistaModelTest(TestCase):
    def setUp(self):
        self.obj = Artista(
            nome='Pink Floyd',
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Artista.object.exists())

    def test_str(self):
        self.assertEqual('Pink Floyd', str(self.obj))