import unittest
from classes import *

class TestControllerBiayaTransportasi(unittest.TestCase):
    def test_hitungHarga(self) -> int:
        listTransport = ControllerBiayaTransportasi([metodeTransportasi(1, "Pesawat", 1000000), metodeTransportasi(2, "Kereta", 100000)])
        harga = metodeTransportasi(1, "Pesawat", 1000000).getHarga() + metodeTransportasi(2, "Kereta", 100000).getHarga()
        self.assertEqual(listTransport.hitungBiaya(), harga)
    
if __name__ == "__main__":
    unittest.main()