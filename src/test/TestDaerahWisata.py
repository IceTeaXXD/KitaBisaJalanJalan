import sqlite3
from classes import *
import unittest

class TestDaerahWisata(unittest.TestCase):
    def test_getID(self):
        self.assertEqual(daerahWisata(1, "Jakarta").getID(), 1)

    def test_getNama(self):
        self.assertEqual(daerahWisata(1, "Jakarta").getNama(), "Jakarta")

    def test_getListDestinasiFromDaerah(self):
        conn = sqlite3.connect('./database/kitabisajalan.db')
        c = conn.cursor()
        query = "select * from lokasiwisata where daerah = ?"
        c.execute(query, str(1))
        self.assertEqual(daerahWisata(1, "Jakarta").getListDestinasiFromDaerah(), c.fetchall())

if __name__ == '__main__':
    unittest.main()
