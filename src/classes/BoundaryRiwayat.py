import sqlite3
from .RiwayatPerjalanan import *
from .MetodeTransportasi import *
from .DestinasiWisata import *

class BoundaryRiwayat:
    def __init__(self):
        self.listRiwayat = []
        self.listRiwayatBerlangsung = []
        
        conn = sqlite3.connect('./database/kitabisajalan.db')
        c = conn.cursor()

        query = "select * from riwayatperjalanan"
        c.execute(query)
        riwayat = c.fetchall()
        for r in riwayat:
            listDestinasi = []
            listTransport = []
            q1 = """
            select ID_Transportasi, Jenis_Transportasi, Harga_Transportasi
            from transportPilihan natural join transportasi
            where ID_Riwayat = ?
            """
            c.execute(q1, (r[0],))
            transport = c.fetchall()

            for t in transport:
                listTransport.append(metodeTransportasi(t[0], t[1], t[2]))
            
            q2 = """
            select ID_Destinasi, Lokasi_Wisata, Daerah, Deskripsi, Gambar
            from destinasiPerjalanan inner join lokasiwisata on ID_Destinasi = ID_Wisata
            where ID_Perjalanan = ?
            """

            c.execute(q2, (r[0],))
            destinasi = c.fetchall()

            for d in destinasi:
                listDestinasi.append(DestinasiWisata(d[0], d[1], d[2], d[3], d[4]))

            q3 = """
            select isi 
            from catatan
            where ID_Catatan = ?
            """

            c.execute(q3, (r[1],))
            catatan = c.fetchall()

            self.listRiwayat.append(RiwayatPerjalanan(r[0], r[1], r[2], r[3], r[4], listDestinasi, listTransport, catatan[0][0]))

        query2 = "SELECT * FROM riwayatperjalanan WHERE DATE('now') between tgl_mulai and tgl_akhir"
        c.execute(query2)
        riwayat2 = c.fetchall()
        for r in riwayat2:
            listDestinasi = []
            listTransport = []
            q1 = """
            select ID_Transportasi, Jenis_Transportasi, Harga_Transportasi
            from transportPilihan natural join transportasi
            where ID_Riwayat = ?
            """
            c.execute(q1, (r[0],))
            transport = c.fetchall()

            for t in transport:
                listTransport.append(metodeTransportasi(t[0], t[1], t[2]))
            
            q2 = """
            select ID_Destinasi, Lokasi_Wisata, Daerah, Deskripsi, Gambar
            from destinasiPerjalanan inner join lokasiwisata on ID_Destinasi = ID_Wisata
            where ID_Perjalanan = ?
            """

            c.execute(q2, (r[0],))
            destinasi = c.fetchall()

            for d in destinasi:
                listDestinasi.append(DestinasiWisata(d[0], d[1], d[2], d[3], d[4]))

            q3 = """
            select isi 
            from catatan
            where ID_Catatan = ?
            """

            c.execute(q3, (r[1],))
            catatan = c.fetchall()

            self.listRiwayatBerlangsung.append(RiwayatPerjalanan(r[0], r[1], r[2], r[3], r[4], listDestinasi, listTransport, catatan[0][0]))
        
        conn.close()

    def getRiwayat(self, tgl = None, id = None) -> list:
        returnList = []

        if(tgl == None and id == None):
            return self.listRiwayatBerlangsung
        elif (tgl != None):
            for r in self.listRiwayat:
                if r.get_tgl_mulai() <= tgl <= r.get_tgl_akhir():
                    returnList.append(r)
            return returnList
        elif(id != None):
            for r in self.listRiwayat:
                if(r.get_id_riwayat() == id):
                    returnList.append(r)
            
            return returnList
        
    def getRiwayatBerlangsung(self, tgl = None, id = None) -> list:
        returnList = []

        if(tgl == None and id == None):
            return self.listRiwayatBerlangsung
        elif (tgl != None):
            for r in self.listRiwayat:
                if r.get_tgl_mulai() <= tgl <= r.get_tgl_akhir():
                    returnList.append(r)
            return returnList
        elif(id != None):
            for r in self.listRiwayat:
                if(r.get_id_riwayat() == id):
                    returnList.append(r)
            
            return returnList