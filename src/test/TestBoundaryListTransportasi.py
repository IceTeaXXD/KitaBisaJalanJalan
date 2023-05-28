import unittest
from classes import *

class TestBoundaryListTransportasi(unittest.TestCase):
    def __init__(self, methodName = "runTest") -> None:
        super().__init__(methodName=methodName)
        self.listTransportasiPilihan = BoundaryListTransportasi().getList()
    
    def test_addToPerjalanan(self):
        self.assertEqual(len(self.listTransportasiPilihan), 0)
        BoundaryListTransportasi.addToPerjalanan(self, metodeTransportasi(1, "Kereta", 50000))
        self.assertEqual(len(self.listTransportasiPilihan), 1)
    
    def test_getList(self):
        BoundaryListTransportasi.addToPerjalanan(self, metodeTransportasi(1, "Kereta", 50000))
        self.assertEqual(len(BoundaryListTransportasi.getList(self)), 1)

    def test_printAll(self):
        BoundaryListTransportasi.addToPerjalanan(self, metodeTransportasi(1, "Kereta", 50000))
        self.assertEqual((self.listTransportasiPilihan[0].getID(), "\b. ", self.listTransportasiPilihan[0].getNama(), "\b", self.listTransportasiPilihan[0].getHarga()), (1, "\b. ", "Kereta", "\b", 50000))

if __name__ == "__main__":
    unittest.main()