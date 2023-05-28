import unittest
from classes import *

class TestBoundaryDestinasiWisata(unittest.TestCase):
    def __init__(self, methodName = "runTest") -> None:
        super().__init__(methodName=methodName)
        self.listDestinasiPilihan = BoundaryDestinasiWisata().getList()

    def test_getList(self):
        BoundaryDestinasiWisata.addToDestinasiPilihan(self, DestinasiWisata(1, "Dufan", "1", "Tempat bermain anak", "dufan.jpg"))
        self.assertEqual(len(BoundaryDestinasiWisata.getList(self)), 1) 
        
    def test_addToDestinasiPilihan(self):
        BoundaryDestinasiWisata.addToDestinasiPilihan(self, DestinasiWisata(1, "Dufan", "1", "Tempat bermain anak", "dufan.jpg"))
        BoundaryDestinasiWisata.addToDestinasiPilihan(self, DestinasiWisata(2, "Pantai Ancol", "1", "Tempat pantai anak", "ancol.jpg"))
        self.assertEqual(len(self.listDestinasiPilihan), 2)
    
    def test_printAll(self):
        BoundaryDestinasiWisata.addToDestinasiPilihan(self, DestinasiWisata(1, "Dufan", "1", "Tempat bermain anak", "dufan.jpg"))
        BoundaryDestinasiWisata.addToDestinasiPilihan(self, DestinasiWisata(2, "Pantai Ancol", "1", "Tempat pantai anak", "ancol.jpg"))
        self.assertEqual((self.listDestinasiPilihan[0].getID(), "\b.", self.listDestinasiPilihan[0].getNamaDestinasi()), (1, "\b.", "Dufan"))
        self.assertEqual((self.listDestinasiPilihan[1].getID(), "\b.", self.listDestinasiPilihan[1].getNamaDestinasi()), (2, "\b.", "Pantai Ancol"))

if __name__ == "__main__":
    unittest.main()