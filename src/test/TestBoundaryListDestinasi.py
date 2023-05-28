import unittest
from classes import *

class TestBoundaryListDestinasi(unittest.TestCase):
    def test_printAll(self):
        listDestinasi = BoundaryListDestinasi([(1, "Dufan","10", 1, "Tempat bermain anak", "dufan.jpg")])
        self.assertEqual((listDestinasi.getDestinasi(1).getID(), "\b.", listDestinasi.getDestinasi(1).getNamaDestinasi(), "\b", listDestinasi.getDestinasi(1).getDeskripsi()),  (1, "\b.", "Dufan", "\b", "Tempat bermain anak"))


    def test_getDestinasi(self):
        listDestinasi = BoundaryListDestinasi([(1, "Dufan","10", 1, "Tempat bermain anak", "dufan.jpg"), (2, "Pantai Ancol", "10", 1, "Tempat pantai anak", "ancol.jpg"), (3, 'Grand Indonesia', '10', 1, 'Ini Mall di Jakarta Pusat', 'GI.jpg')])
        self.assertEqual(listDestinasi.getDestinasi(1).getNamaDestinasi(), "Dufan")
    
    def test_getList(self):
        listDestinasi = BoundaryListDestinasi([(1, "Dufan","10", 1, "Tempat bermain anak", "dufan.jpg"), (2, "Pantai Ancol", "10", 1, "Tempat pantai anak", "ancol.jpg"), (3, 'Grand Indonesia', '10', 1, 'Ini Mall di Jakarta Pusat', 'GI.jpg')])
        self.assertEqual(len(listDestinasi.getList()), 3)

if __name__ == "__main__":
    unittest.main()