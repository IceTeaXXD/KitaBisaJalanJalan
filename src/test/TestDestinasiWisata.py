from classes import *
import unittest

class TestDestinasiWisata(unittest.TestCase):
    def test_makeList(self):
        self.assertEqual(DestinasiWisata(6, "PVJ", 2, "Ini mall gess", "pvj.jpg").makeList(), [6, "PVJ", 2, "pvj.jpg"])

    def test_getID(self):
        self.assertEqual(DestinasiWisata(6, "PVJ", 2, "Ini mall gess", "pvj.jpg").getID(), 6)

    def test_getNamaDestinasi(self):
        self.assertEqual(DestinasiWisata(6, "PVJ", 2, "Ini mall gess", "pvj.jpg").getNamaDestinasi(), "PVJ")

    def test_getDeskripsi(self):
        self.assertEqual(DestinasiWisata(6, "PVJ", 2, "Ini mall gess", "pvj.jpg").getDeskripsi(), "Ini mall gess")

    def test_getGambar(self):
        self.assertEqual(DestinasiWisata(6, "PVJ", 2, "Ini mall gess", "pvj.jpg").getGambar(), "pvj.jpg")

if __name__ == '__main__':
    unittest.main()