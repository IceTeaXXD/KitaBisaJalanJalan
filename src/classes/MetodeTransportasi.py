class metodeTransportasi:
    def __init__(self, idTransportasi, namaTransportasi, harga):
        self.idTransportasi = idTransportasi
        self.namaTransportasi = namaTransportasi
        self.harga = harga

    def getID(self):
        return self.idTransportasi
    
    def getNama(self):
        return self.namaTransportasi

    def getHarga(self):
        return self.harga