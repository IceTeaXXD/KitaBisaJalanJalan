import sqlite3
from classes import *
import unittest

class TestListTransportasi(unittest.TestCase):
    def test_getList(self):
        self.assertEqual(len(ListTransportasi().getList()), 4)
        self.assertEqual(ListTransportasi().getList()[0].getID(), 1)
        self.assertEqual(ListTransportasi().getList()[0].getNama(), "Kereta")
        
    def test_getTransportasi(self, idx=2):
        self.assertEqual(ListTransportasi().getTransportasi(idx).getID(), 2)
        self.assertEqual(ListTransportasi().getTransportasi(idx).getNama(), "Pesawat")
    
    def test_printAll(self):
        listTransport = ListTransportasi().getList()
        for i in range(1, len(listTransport) + 1):
            resultPrint = listTransport[i - 1].getID(), "\b", listTransport[i - 1].getNama(), "harga per km:", listTransport[i - 1].getHarga()
            expectedPrint = i, "\b", ListTransportasi().getTransportasi(i).getNama(), "harga per km:", ListTransportasi().getTransportasi(i).getHarga()
            self.assertEqual(resultPrint, expectedPrint)

if __name__ == '__main__':
    unittest.main()