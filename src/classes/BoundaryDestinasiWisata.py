from .DestinasiWisata import *
# Destinasi Wisata yang Dipilih
class BoundaryDestinasiWisata:
    def __init__(self):
        self.listDestinasiPilihan = []

    def addToDestinasiPilihan(self, obj: DestinasiWisata):
        self.listDestinasiPilihan.append(obj)

    def getList(self):
        return self.listDestinasiPilihan

    def printAll(self):
        print("idx. nama_destinasi")
        for l in self.listDestinasiPilihan:
            print(l.getID(), "\b.", l.getNamaDestinasi())
