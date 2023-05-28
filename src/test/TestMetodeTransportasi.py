from classes import *
import unittest

class TestMetodeTransportasi(unittest.TestCase):
    def test_getID(self):
        self.assertEqual(metodeTransportasi(3, "Mobil", 10000).getID(), 3)

    def test_getNama(self):
        self.assertEqual(metodeTransportasi(3, "Mobil", 10000).getNama(), "Mobil")

    def test_getHarga(self):
        self.assertEqual(metodeTransportasi(3, "Mobil", 10000).getHarga(), 10000)

if __name__ == '__main__':
    unittest.main()
