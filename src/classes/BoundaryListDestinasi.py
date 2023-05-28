from .DestinasiWisata import *

#  Destinasi Wisata dari Daerah Wisata yang bersesuaian
class BoundaryListDestinasi:
    def __init__(self, listDestinasi):
        self.listDestinasi = []

        for d in listDestinasi:
            dest = DestinasiWisata(d[0], d[1], d[2], d[4], d[5])
            self.listDestinasi.append(dest)

    def printAll(self):
        print("idx. nama_destinasi (deskripsi)")
        for dest in self.listDestinasi:
            print(dest.getID(), "\b. ", dest.getNamaDestinasi(), "(", dest.getDeskripsi(), ")")

    def getDestinasi(self, idx: int) -> DestinasiWisata:
        # Ambil destinasi dengan id destinasi idx
        for dest in self.listDestinasi:
            if(dest.getID() == idx):
                return dest
    
    def getList(self) -> list:
        return self.listDestinasi