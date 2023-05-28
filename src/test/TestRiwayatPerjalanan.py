from classes import *
import unittest

class TestRiwayatPerjalanan(unittest.TestCase):
    def test_get_id_riwayat(self):
        self.assertEqual(RiwayatPerjalanan(1, 1, "2020-10-10", "2020-10-12", 10000, [DestinasiWisata(6, 'PVJ', 2, 'Ini mall gess', 'pvj.jpg')], [metodeTransportasi(3, "Mobil", 10000)], "haii").get_id_riwayat(), 1)

    def test_get_id_catatan(self):
        self.assertEqual(RiwayatPerjalanan(1, 1, "2020-10-10", "2020-10-12", 10000, [DestinasiWisata(6, 'PVJ', 2, 'Ini mall gess', 'pvj.jpg')], [metodeTransportasi(3, "Mobil", 10000)], "haii").get_id_catatan(), 1)

    def test_get_tgl_mulai(self):
        self.assertEqual(RiwayatPerjalanan(1, 1, "2020-10-10", "2020-10-12", 10000, [DestinasiWisata(6, 'PVJ', 2, 'Ini mall gess', 'pvj.jpg')], [metodeTransportasi(3, "Mobil", 10000)], "haii").get_tgl_mulai(), "2020-10-10")
        
    def test_get_tgl_akhir(self):
        self.assertEqual(RiwayatPerjalanan(1, 1, "2020-10-10", "2020-10-12", 10000, [DestinasiWisata(6, 'PVJ', 2, 'Ini mall gess', 'pvj.jpg')], [metodeTransportasi(3, "Mobil", 10000)], "haii").get_tgl_akhir(), "2020-10-12")
    
    def test_get_biaya_perjalanan(self):
        self.assertEqual(RiwayatPerjalanan(1, 1, "2020-10-10", "2020-10-12", 10000, [DestinasiWisata(6, 'PVJ', 2, 'Ini mall gess', 'pvj.jpg')], [metodeTransportasi(3, "Mobil", 10000)], "haii").get_biaya_perjalanan(), 10000)

    def test_get_list_destinasi(self):
        destinasi = DestinasiWisata(6, 'PVJ', 2, 'Ini mall gess', 'pvj.jpg')
        perjalanan = RiwayatPerjalanan(1, 2, "2020-10-10", "2020-10-12", 10000, [destinasi], [metodeTransportasi(3, "Mobil", 10000)], "haii")
        self.assertEqual(perjalanan.get_list_destinasi(), [destinasi])
    
    def test_get_list_transportasi(self):
        transportasi = metodeTransportasi(3, "Mobil", 10000)
        perjalanan = RiwayatPerjalanan(1, 1, "2020-10-10", "2020-10-12", 10000, [DestinasiWisata(6, 'PVJ', 2, 'Ini mall gess', 'pvj.jpg')], [transportasi], "haii")
        self.assertEqual(perjalanan.get_list_transportasi(), [transportasi])

    def test_get_catatan(self):
        self.assertEqual(RiwayatPerjalanan(1, 1, "2020-10-10", "2020-10-12", 10000, [DestinasiWisata(6, 'PVJ', 2, 'Ini mall gess', 'pvj.jpg')], [metodeTransportasi(3, "Mobil", 10000)], "haii").get_catatan(), "haii")

    def test_set_catatan(self):
        catatan = "ini catatan yang telah diperbarui"
        perjalanan = RiwayatPerjalanan(1, 1, "2020-10-10", "2020-10-12", 10000, [DestinasiWisata(6, 'PVJ', 2, 'Ini mall gess', 'pvj.jpg')], [metodeTransportasi(3, "Mobil", 10000)], "haii")
        perjalanan.set_catatan(catatan)
        self.assertEqual(perjalanan.get_catatan(), catatan)

    def test_print(self):
        destinasi = [DestinasiWisata(6, 'PVJ', 2, 'Ini mall gess', 'pvj.jpg')]
        transportasi = [metodeTransportasi(3, "Mobil", 10000)]
        riwayat = RiwayatPerjalanan(1, 1, "2023-04-15", "2023-04-20", 1000000, destinasi, transportasi, "ini catatan")
        resultPrint = "ID Catatan:", "\b", riwayat.get_id_catatan(), "\n", "ID Riwayat:", "\b", riwayat.get_id_riwayat(), "\n", "Tanggal:", "\b", riwayat.get_tgl_mulai(), "\b", "s.d.", "\b", riwayat.get_tgl_akhir(), "\n", "Biaya:", "\b", riwayat.get_biaya_perjalanan(), "\n", "List Destinasi", "\n", destinasi[0].getID(), "\b.", destinasi[0].getNamaDestinasi(), "\n", "List Transportasi", "\n", transportasi[0].getID(), "\b.", transportasi[0].getNama(), "\b", "harga per km:", "\b", transportasi[0].getHarga(), "\n", "Catatan Anda:", "\n", riwayat.get_catatan()
        expected = "ID Catatan:", "\b", 1, "\n", "ID Riwayat:", "\b", 1, "\n", "Tanggal:", "\b", "2023-04-15", "\b", "s.d.", "\b", "2023-04-20", "\n", "Biaya:", "\b", 1000000, "\n", "List Destinasi", "\n", 6, "\b.", "PVJ", "\n", "List Transportasi", "\n", 3, "\b.", "Mobil", "\b", "harga per km:", "\b", 10000, "\n", "Catatan Anda:", "\n", "ini catatan"
        self.assertEqual(resultPrint, expected)

if __name__ == '__main__':
    unittest.main()