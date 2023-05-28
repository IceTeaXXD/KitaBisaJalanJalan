from .MetodeTransportasi import *

class BoundaryListTransportasi:
    def __init__(self):
        self.listTransportasiPilihan = []
    
    def addToPerjalanan(self, obj: metodeTransportasi):
        self.listTransportasiPilihan.append(obj)

    def getList(self):
         return self.listTransportasiPilihan

    def printAll(self):
            print("idx. nama_transport")
            for t in self.listTransportasiPilihan:
                print(t.getID(), "\b.", t.getNama(), "harga per km:", t.getHarga())