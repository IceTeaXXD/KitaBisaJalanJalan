import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

arr_destinasi = ['Bali', 'Lombok', 'Pulau Derawan', 'Pulau Komodo', 'Pulau Raja Ampat', 'Pulau Wakatobi', 'Pulau Bunaken', 'Pulau Togian', 'Pulau Ternate', 'Pulau Tidung', 'Pulau Banyak', 'Pulau Sangihe', 'Pulau Siau', 'Pulau Siau Tagulandang Biaro', 'Pulau Siau Tagulandang', 'Pulau Siau Tagulandang Utara', 'Pulau Siau Tagulandang Selatan', 'Pulau Siau Tagulandang Tengah', 'Pulau Siau Tagulandang Timur', 'Pulau Siau Tagulandang Barat', 'Pulau Siau Tagulandang Barat Daya', 'Pulau Siau Tagulandang Barat Laut', 'Pulau Siau Tagulandang Barat Tengah', 'Pulau Siau Tagulandang Barat Utara', 'Pulau Siau Tagulandang Tenggara', 'Pulau Siau Tagulandang Timur Laut', 'Pulau Siau Tagulandang Timur Tengah', 'Pulau Siau Tagulandang Timur Utara', 'Pulau Siau Tagulandang Utara Daya', 'Pulau Siau Tagulandang Utara Laut', 'Pulau Siau Tagulandang Utara Tengah', 'Pulau Siau Tagulandang Utara Utara', 'Pulau Siau Tagulandang Selatan Daya', 'Pulau Siau Tagulandang Selatan Laut', 'Pulau Siau Tagulandang Selatan Tengah', 'Pulau Siau Tagulandang Selatan Utara', 'Pulau Siau Tagulandang Tengah Daya', 'Pulau Siau Tagulandang Tengah Laut', 'Pulau Siau Tagulandang Tengah Teng']
arr_kendaraan = ['Pesawat', 'Kapal', 'Kereta Api', 'Bus', 'Mobil', 'Motor', 'Sepeda', 'Sepeda Motor', 'Sepeda Motor Listrik', 'Sepeda M']

class CatatanWindow(QDialog):
    def __init__(self):
        super(CatatanWindow, self).__init__()
        loadUi("./interface/ui/catatan.ui", self)

        self.setFixedSize(1512, 982)
        
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setContentsMargins(100, 230, 950, 250)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)
        self.setLayout(self.verticalLayout)

    def setDestinasi(self, data, tgl):
        self.textEdit.setText("")

        # Parse tanggal
        parseDate = tgl.split("-")
        
        # Angka -> Bulan
        if(parseDate[1] == "01"):
            parseDate[1] = "JAN"
        elif(parseDate[1] == "02"):
            parseDate[1] = "FEB"
        elif(parseDate[1] == "03"):
            parseDate[1] = "MAR"
        elif(parseDate[1] == "04"):
            parseDate[1] = "APR"
        elif(parseDate[1] == "05"):
            parseDate[1] = "MEI"
        elif(parseDate[1] == "06"):
            parseDate[1] = "JUN"
        elif(parseDate[1] == "07"):
            parseDate[1] = "JUL"
        elif(parseDate[1] == "08"):
            parseDate[1] = "AGT"
        elif(parseDate[1] == "09"):
            parseDate[1] = "SEP"
        elif(parseDate[1] == "10"):
            parseDate[1] = "OKT"
        elif(parseDate[1] == "11"):
            parseDate[1] = "NOV"
        else:
            parseDate[1] = "DES"
 
        # Set Bulan dan Tanggal
        self.Bulan.setText(parseDate[1])
        self.Tanggal.setText(parseDate[2])

        listDestinasi = []
        for riwayat in data:
            list = riwayat.get_list_destinasi()
            for destinasi in list:
                listDestinasi.append(destinasi.getNamaDestinasi())

        listKendaraan = []
        for riwayat in data:
            list = riwayat.get_list_transportasi()
            for kendaraan in list:
                listKendaraan.append(kendaraan.getNama())

        sum = 0
        for riwayat in data:
            sum += riwayat.get_biaya_perjalanan()

        # set the text edit to anything in the database
        catatan = ""
        for riwayat in data:
            catatan = riwayat.get_catatan()
        
        if catatan != "":
            self.textEdit.setText(catatan)

        # make container for each destinasi
        destinasi = QLabel()
        destinasi.setFixedWidth(400)
        destinasi.setFixedHeight(100)
        destinasi.setStyleSheet("background-color: #03EF62; border-radius: 10px; ")
        destinasi.setAlignment(Qt.AlignTop)
        
        # destinasi box
        destinasi_box = QVBoxLayout(destinasi)
        destinasi_box.setContentsMargins(0,0,0,0)
        destinasi_box.setSpacing(0)

        judul_destinasi = QLabel("Destinasi Wisata")
        judul_destinasi.setFixedSize(400, 50)
        judul_destinasi.setStyleSheet("background-color: #884CFD; color: #ffffff; border-radius: 10px 10px 0px 0px;")
        judul_destinasi.setAlignment(Qt.AlignCenter)
        destinasi_box.addWidget(judul_destinasi)

        # define each element in arr destinasi
        for j in range (len(listDestinasi)):
            destinasi_label = QLabel(listDestinasi[j])
            destinasi_label.setFixedSize(400, 50)
            destinasi_label.setStyleSheet("background-color: #FFFFFF; color: #000000; border-radius: 10px; margin-left : 10px ; margin-right : 10px ; margin-top : 10px ; margin-bottom : 10px ;")
            destinasi_label.setAlignment(Qt.AlignCenter)
            destinasi_box.addWidget(destinasi_label)
            # get height of destinasi
            destinasi_height = destinasi_label.height()
            # get height of destinasi box
            destinasi_box_height = destinasi.height()
            destinasi.setFixedHeight(destinasi_height + destinasi_box_height)
            
        # make the destinasi label expand horizontally
        destinasi.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # make container for each kendaraan
        kendaraan = QLabel()
        kendaraan.setFixedWidth(400)
        kendaraan.setFixedHeight(100)
        # kendaraan.setFixedSize(465, 500)
        kendaraan.setStyleSheet("background-color: #03EF62; border-radius: 10px; ")
        kendaraan.setAlignment(Qt.AlignTop)

        # kendaraan box
        kendaraan_box = QVBoxLayout(kendaraan)
        kendaraan_box.setContentsMargins(0,0,0,0)
        kendaraan_box.setSpacing(0)

        judul_kendaraan = QLabel("Kendaraan")
        judul_kendaraan.setFixedSize(400, 50)
        judul_kendaraan.setStyleSheet("background-color: #884CFD; color: #ffffff; border-radius: 10px 10px 0px 0px;")
        judul_kendaraan.setAlignment(Qt.AlignCenter)
        kendaraan_box.addWidget(judul_kendaraan)
        
        # define each element in arr kendaraan
        for j in range (len(listKendaraan)):
            kendaraan_label = QLabel(listKendaraan[j])
            kendaraan_label.setFixedSize(400, 50)
            kendaraan_label.setStyleSheet("background-color: #FFFFFF; color: #000000; border-radius: 10px; margin-left : 10px ; margin-right : 10px ; margin-top : 10px ; margin-bottom : 10px ;")
            kendaraan_label.setAlignment(Qt.AlignCenter)
            kendaraan_box.addWidget(kendaraan_label)
            # get height of kendaraan
            kendaraan_height = kendaraan_label.height()
            # get height of kendaraan box
            kendaraan_box_height = kendaraan.height()
            kendaraan.setFixedHeight(kendaraan_height + kendaraan_box_height)
        # kendaraan.setFixedHeight(kendaraan_height - kendaraan_box_height + 50)

            # make the kendaraan label expand horizontally
        kendaraan.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # make container for each kendaraan
        biaya = QLabel()
        biaya.setFixedWidth(400)
        biaya.setFixedHeight(100)
        # biaya.setFixedSize(465, 500)
        biaya.setStyleSheet("background-color: #03EF62; border-radius: 10px; ")
        biaya.setAlignment(Qt.AlignTop)

        # biaya box
        biaya_box = QVBoxLayout(biaya)
        biaya_box.setContentsMargins(0,0,0,0)
        biaya_box.setSpacing(0)
        

        judul_biaya = QLabel("biaya")
        judul_biaya.setFixedSize(400, 50)
        judul_biaya.setStyleSheet("background-color: #884CFD; color: #ffffff; border-radius: 10px 10px 0px 0px;")
        judul_biaya.setAlignment(Qt.AlignCenter)
        biaya_box.addWidget(judul_biaya)

        # deskripsi biaya
        biaya_deskripsi = QLabel(f"Rp {sum}")
        biaya_deskripsi.setFixedSize(400, 50)
        biaya_deskripsi.setStyleSheet("background-color: #FFFFFF; color: #000000; border-radius: 10px; margin-left : 10px ; margin-right : 10px ; margin-top : 10px ; margin-bottom : 10px ;")
        biaya_deskripsi.setAlignment(Qt.AlignCenter)
        biaya_box.addWidget(biaya_deskripsi)

        # add to grid layout
        self.gridLayout.addWidget(destinasi, 0, 0, 1, 1)
        # insert below the destinasi
        self.gridLayout.addWidget(kendaraan, 1, 0, 1, 1)
        # insert below the kendaraan
        self.gridLayout.addWidget(biaya, 2, 0, 1, 1)

#make main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CatatanWindow()
    window.show()
    sys.exit(app.exec_())