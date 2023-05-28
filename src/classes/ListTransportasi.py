import sqlite3
from .MetodeTransportasi import *
# Semua transportasi pada Database
class ListTransportasi:
    def __init__(self):
        conn = sqlite3.connect('./database/kitabisajalan.db')
        c = conn.cursor()
        query = """select * from transportasi"""
        c.execute(query)
        self.listTransport = []
        for t in c.fetchall():
            obj = metodeTransportasi(t[0], t[1], t[2])
            self.listTransport.append(obj)
        # isi list transport dari query
        conn.close()

    def getList(self):
        return self.listTransport
    
    def getTransportasi(self, idx):
        # Ambil transport dengan id idx
        # kembalikan
        for t in self.listTransport:
            if(t.getID() == idx):
                return t
        return
    
    def printAll(self):
        print("idx. transport_name")
        for t in self.listTransport:
            print(t.getID(), "\b.", t.getNama(), "harga per km:", t.getHarga())