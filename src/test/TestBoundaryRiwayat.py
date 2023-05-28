import unittest
import sqlite3
from classes import *

class TestBoundaryRiwayat(unittest.TestCase):
    def test_getRiwayat(self):
        listRiwayat = BoundaryRiwayat().getRiwayat()
        query = "select * from riwayatperjalanan where DATE('now') between tgl_mulai and tgl_akhir"
        conn = sqlite3.connect('./database/kitabisajalan.db')
        c = conn.cursor()
        c.execute(query)
        self.assertEqual(len(listRiwayat), len(c.fetchall())) # gak tau masi bingung
        c.close()

    def test_getRiwayatBerlangsung(self):
        listRiwayatBerlangsung = BoundaryRiwayat().getRiwayatBerlangsung()
        query = "select * from riwayatperjalanan where DATE('now') between tgl_mulai and tgl_akhir"
        conn = sqlite3.connect('./database/kitabisajalan.db')
        c = conn.cursor()
        c.execute(query)
        self.assertEqual(len(listRiwayatBerlangsung), len(c.fetchall())) # ini juga gak tau
        c.close()


if __name__ == "__main__":
    unittest.main()