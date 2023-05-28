import sqlite3
from classes import *
import unittest

class TestControllerCatatan(unittest.TestCase):
    def test_saveCatatan(self):
        cc = controllerCatatan(1, "Ini catatan pertama")
        cc.saveCatatan("Ini catatan kedua")
        assert cc.catatan == "Ini catatan kedua"

    def test_submitCatatan(self):
        catatan = controllerCatatan(1, "Ini adalah catatan")
        catatan.saveCatatan("Catatan baru Aku")
        catatan.submitCatatan()

        # check that the catatan was updated in the database
        conn = sqlite3.connect('./database/kitabisajalan.db')
        c = conn.cursor()
        query = """select isi from catatan where ID_Catatan = 1"""
        c.execute(query)
        result = c.fetchone()[0]
        self.assertEqual(result, "Catatan baru Aku")
    
    def test_getCatatan(self):
        conn = sqlite3.connect('./database/kitabisajalan.db')
        c = conn.cursor()
        query = """select * from catatan where ID_Catatan = :id"""
        c.execute(query, {'id': 1})
        self.assertEqual(controllerCatatan(1, "Ini adalah catatan baru Aku").getCatatan(), c.fetchall())

if __name__ == '__main__':
    unittest.main()