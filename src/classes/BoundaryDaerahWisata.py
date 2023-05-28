import sqlite3
from .DaerahWisata import *
# List Daerah Wisata dari database
class BoundaryDaerahWisata:
    def __init__(self):
        conn = sqlite3.connect("./database/kitabisajalan.db")
        c = conn.cursor()
        q = "select * from daerah"
        c.execute(q)
        self.listDaerahWisata = []
        for daerah in c.fetchall():
            obj = daerahWisata(daerah[0], daerah[1])
            self.listDaerahWisata.append(obj)
        conn.close()

    def getListDaerah(self):
        return self.listDaerahWisata
    
    def getDaerah(self, idx) -> daerahWisata:
        # idx adalah id daerah wisata
        for daerah in self.listDaerahWisata:
            if daerah.getID() == int(idx):
                return daerah
            
    def printAll(self):
        print("idx. nama_daerah")
        for daerah in self.listDaerahWisata:
            print(daerah.getID(), "\b. ", daerah.getNama())
