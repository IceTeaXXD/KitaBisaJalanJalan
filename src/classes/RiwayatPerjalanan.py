class RiwayatPerjalanan:
    def __init__(self, idRiwayat, idCatatan, tglMulai, tglAkhir, biayaPerjalanan, listDestinasi, listTransportasi, catatan):
        self.idRiwayat = idRiwayat
        self.idCatatan = idCatatan
        self.tglMulai = tglMulai
        self.tglAkhir = tglAkhir
        self.biayaPerjalanan = biayaPerjalanan
        self.listDestinasi = listDestinasi
        self.listTransportasi = listTransportasi
        self.catatan = catatan

    def get_id_riwayat(self):
        return self.idRiwayat

    def get_id_catatan(self):
        return self.idCatatan

    def get_tgl_mulai(self):
        return self.tglMulai

    def get_tgl_akhir(self):
        return self.tglAkhir

    def get_biaya_perjalanan(self):
        return self.biayaPerjalanan

    def get_list_destinasi(self):
        return self.listDestinasi

    def get_list_transportasi(self):
        return self.listTransportasi
    
    def get_catatan(self):
        return self.catatan
    
    def set_catatan(self, catatan):
        self.catatan = catatan
    
    def print(self):
        print(f"ID Riwayat: {self.idRiwayat}")
        print(f"ID Catatan: {self.idCatatan}")
        print(f"Tanggal: {self.tglMulai} s.d. {self.tglAkhir}")
        print(f"Biaya: {self.biayaPerjalanan}")
        print("List Destinasi")
        for d in self.listDestinasi:
            print(d.getID(), "\b.", d.getNamaDestinasi())

        print("List Transportasi")
        for t in self.listTransportasi:
            print(t.getID(), "\b.", t.getNama(), "harga per km:", t.getHarga())
        print("Catatan Anda: ")
        print(self.catatan)