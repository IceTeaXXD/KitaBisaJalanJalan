import sqlite3
class ControllerPerjalanan:
    def __init__(self, biayaTransport: int, listDestinasiPilihan: list, listTransportasiPilihan: list, tglAwal: str, tglAkhir):
        self.biayaTransport = biayaTransport
        self.listDestinasiPilihan = listDestinasiPilihan
        self.listTransportasiPilihan = listTransportasiPilihan
        self.tglAwal = tglAwal
        self.tglAkhir = tglAkhir

    def makePerjalanan(self):
        conn = sqlite3.connect('./database/kitabisajalan.db')
        c = conn.cursor()
        c.execute("select * from riwayatperjalanan")
        idRiwayat = len(c.fetchall()) + 1

        # Ke dalam tabel riwayatperjalanan
        queryRiwayat = "insert into riwayatperjalanan values (?, ?, ?, ?, ?)"
        with conn:
            c.execute(queryRiwayat, (idRiwayat, idRiwayat, self.tglAwal, self.tglAkhir, self.biayaTransport))

        # Ke dalam tabel listdestinasipilihan
        for dest in self.listDestinasiPilihan:
            queryDestinasiPerjalanan = """
            insert into destinasiPerjalanan values
            (?,?) """

            with conn:
                c.execute(queryDestinasiPerjalanan, (idRiwayat, str(dest.getID())))

        # ke dalam tabel transportasipilihan
        i = 1
        for tp in self.listTransportasiPilihan:
            queryTransportasiPilihan = """
            insert into transportPilihan values
            (?,?,?)"""
            with conn:
                c.execute(queryTransportasiPilihan, (idRiwayat, tp.getID(), i))
            i+=1

        queryCatatan = """
        insert into catatan values
        (?, ?, ?, '')
        """

        with conn:
            c.execute(queryCatatan, (idRiwayat,self.tglAwal, self.tglAkhir))

        print("Sukses menyimpan perjalanan!")

        conn.close()