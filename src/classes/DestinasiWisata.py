class DestinasiWisata:
    # Konstruktor Destinasi Wisata 
    def __init__(self, idDestinasi, destinasi, daerah, deskripsi, gambar):
        self.__idDestinasi = idDestinasi
        self.__destinasi = destinasi
        self.__daerah = daerah
        self.__deskripsi = deskripsi
        self.__gambar = gambar
    
    # Mengembalikan sebuah tipe Destinasi Wisata yang
    # nantinya dapat di-append ke suatu list yang lebih besar
    # untuk dijadikan array pilihan
    def makeList(self):
        return [self.__idDestinasi, self.__destinasi, self.__daerah, self.__gambar]
    
    def getID(self):
        return self.__idDestinasi
    
    def getNamaDestinasi(self):
        return self.__destinasi
    
    def getDeskripsi(self):
        return self.__deskripsi
    
    def getGambar(self):
        return self.__gambar