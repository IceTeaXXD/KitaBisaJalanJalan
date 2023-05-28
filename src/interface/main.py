import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from datetime import date

from .welcome import*
from .home import *
from .catatan import *
from .pilihDaerah import *
from .pilihDestinasi import *
from .riwayatPerjalanan import *
from .perkiraanBiayaTransportasi import *
from .sedangBerlangsung import *
from .pilihTanggalPerjalanan import *
from .image import *

from classes import *

class MainApplication(QApplication):
    def __init__(self, argv):
        super(MainApplication, self).__init__(argv)

        # Initialize the windows
        self.welcome = WelcomeWindow()
        self.home = HomeWindow()
        self.catatan = CatatanWindow()
        self.pilihDaerah = pilihDaerahWindow()
        self.pilihDestinasi = pilihDestinasiWindow()
        self.riwayatPerjalanan = riwayatPerjalananWindow()
        self.perkiraanBiayaTransportasi = PerkiraanBiayaTransportasiWindow()
        self.sedangBerlangsung = sedangBerlangsungWindow()
        self.pilihTanggalPerjalanan = pilihTanggalPerjalananWindow()
        
        # Initialize the widgets for the main window and pages
        self.widget = QtWidgets.QStackedWidget()
        self.widget.addWidget(self.welcome)
        self.widget.addWidget(self.home)
        self.widget.addWidget(self.catatan)
        self.widget.addWidget(self.pilihDaerah)
        self.widget.addWidget(self.pilihDestinasi)
        self.widget.addWidget(self.riwayatPerjalanan)
        self.widget.addWidget(self.perkiraanBiayaTransportasi)
        self.widget.addWidget(self.sedangBerlangsung)
        self.widget.addWidget(self.pilihTanggalPerjalanan)
        
        # Set the main window size
        self.widget.setFixedWidth(1512)
        self.widget.setFixedHeight(982)
        self.widget.show()

        # Button Handlers
        self.welcome.next_button.clicked.connect(self.welcome_next_button_clicked)
        self.home.button_baru.clicked.connect(self.button_baru_clicked)
        self.pilihDaerah.back_button.clicked.connect(self.pilihDaerah_back_button_clicked)
        self.pilihDaerah.next_button.clicked.connect(self.pilihDaerah_next_button_clicked)
        self.pilihDestinasi.back_button.clicked.connect(self.pilihDestinasiback_button_clicked)
        self.pilihDestinasi.next_button.clicked.connect(self.pilihDestinasinext_button_clicked)
        self.perkiraanBiayaTransportasi.back_button.clicked.connect(self.perkiraanBiayaTransportasi_back_button_clicked)
        self.perkiraanBiayaTransportasi.next_button.clicked.connect(self.perkiraanBiayaTransportasi_next_button_clicked)
        self.riwayatPerjalanan.back_button.clicked.connect(self.riwayatPerjalanan_back_button_clicked)
        self.catatan.back_button.clicked.connect(self.back_button_clicked)  
        self.pilihTanggalPerjalanan.back_button.clicked.connect(self.pilihTanggalPerjalanan_back_button_clicked)
        self.pilihTanggalPerjalanan.submit.clicked.connect(self.submit_clicked)
        self.sedangBerlangsung.back_button.clicked.connect(self.sedangBerlangsung_back_button_clicked)
        self.home.button_riwayat.clicked.connect(self.button_riwayat_clicked)
        self.home.button_sedangberlangsung.clicked.connect(self.sedangberlangsung_clicked)
        self.riwayatPerjalanan.submit.clicked.connect(self.submit_riwayat_clicked)
        self.catatan.submit.clicked.connect(self.submit_catatan_clicked)

    def welcome_next_button_clicked(self):
        # get the username from the welcome window
        username = self.welcome.textEdit.toPlainText()
        if username == "":
            # error dialog box
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Username Belum Diisi!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        self.pilihDaerah.label_3.setText(f'Halo, {username}! Mau Kemana Kita ?')
        self.widget.setCurrentWidget(self.home)

    def button_baru_clicked(self):
        self.widget.setCurrentWidget(self.pilihDaerah)

    def pilihDaerah_next_button_clicked(self):
        if self.pilihDaerah.selectedID() == None:
            # error dialog box
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Daerah Belum Dipilih!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        self.pilihDestinasi.reset()

        # get daerah from id
        daerahpilihan = self.pilihDaerah.daerahwisata.getDaerah(self.pilihDaerah.selectedID())
        listDestinasi = BoundaryListDestinasi(daerahpilihan.getListDestinasiFromDaerah())
        self.pilihDestinasi.setDaerah(listDestinasi.getList())

        self.widget.setCurrentWidget(self.pilihDestinasi)

    def pilihDaerah_back_button_clicked(self):
        self.widget.setCurrentWidget(self.home)

    def pilihDestinasiback_button_clicked(self):
        self.widget.setCurrentWidget(self.pilihDaerah)

    def pilihDestinasinext_button_clicked(self):
        checked = self.pilihDestinasi.getNameChecked()
        if (len(checked) == 0):
            # error dialog box
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Destinasi Belum Dipilih!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        
        daerahpilihan = self.pilihDaerah.daerahwisata.getDaerah(self.pilihDaerah.selectedID())
        listDestinasi = BoundaryListDestinasi(daerahpilihan.getListDestinasiFromDaerah())
        listDestinasiPilihan = BoundaryDestinasiWisata()

        for i in checked:
            for j in range(len(listDestinasi.getList())):
                if i == listDestinasi.getList()[j].getNamaDestinasi():
                    listDestinasiPilihan.addToDestinasiPilihan(listDestinasi.getList()[j])

        self.perkiraanBiayaTransportasi.reset()
        self.perkiraanBiayaTransportasi.setDestinasi(listDestinasiPilihan.getList())
        self.widget.setCurrentWidget(self.perkiraanBiayaTransportasi)

    def perkiraanBiayaTransportasi_back_button_clicked(self):
        self.widget.setCurrentWidget(self.pilihDestinasi)

    def perkiraanBiayaTransportasi_next_button_clicked(self):
        self.widget.setCurrentWidget(self.pilihTanggalPerjalanan)

    def button_riwayat_clicked(self):
        self.widget.setCurrentWidget(self.riwayatPerjalanan)

    def sedangberlangsung_clicked(self):
        self.sedangBerlangsung.setSedangBerlangsung(BoundaryRiwayat().getRiwayatBerlangsung(tgl = str(date.today())))
        self.widget.setCurrentWidget(self.sedangBerlangsung)

    def sedangBerlangsung_back_button_clicked(self):
        self.widget.setCurrentWidget(self.home)
        
    def riwayatPerjalanan_back_button_clicked(self):
        self.widget.setCurrentWidget(self.home)

    def back_button_clicked(self):
        self.widget.setCurrentWidget(self.home)

    def pilihTanggalPerjalanan_back_button_clicked(self):
        self.widget.setCurrentWidget(self.perkiraanBiayaTransportasi)

    def submit_clicked(self):
        start_date, end_date = self.pilihTanggalPerjalanan.getDateSelected()

        checked = self.perkiraanBiayaTransportasi.checkedTransportasiHarga()

        listTransportasi = ListTransportasi()
        transportPilihan = BoundaryListTransportasi()

        for t in checked:
            transportPilihan.addToPerjalanan(listTransportasi.getTransportasi(t[0]))

        controllerBiaya = ControllerBiayaTransportasi(transportPilihan.getList())
        biayaTransport = controllerBiaya.hitungBiaya()

        daerahpilihan = self.pilihDaerah.daerahwisata.getDaerah(self.pilihDaerah.selectedID())
        listDestinasi = BoundaryListDestinasi(daerahpilihan.getListDestinasiFromDaerah())
        listDestinasiPilihan = BoundaryDestinasiWisata()
        checked_dest = self.pilihDestinasi.getNameChecked()
        for i in checked_dest:
            for j in range(len(listDestinasi.getList())):
                if i == listDestinasi.getList()[j].getNamaDestinasi():
                    listDestinasiPilihan.addToDestinasiPilihan(listDestinasi.getList()[j])

        if end_date is None:
            end_date = start_date
        add = ControllerPerjalanan(biayaTransport, listDestinasiPilihan.getList(), transportPilihan.getList(), start_date, end_date)
        add.makePerjalanan()
    
        self.widget.setCurrentWidget(self.home)

    def submit_riwayat_clicked(self):
        riwayat = self.riwayatPerjalanan.getRiwayat()
        self.catatan.setDestinasi(riwayat, self.riwayatPerjalanan.selectDate)
        self.widget.setCurrentWidget(self.catatan)

    def submit_catatan_clicked(self):
        riwayat = self.riwayatPerjalanan.getRiwayat()
        listCatatan = []
        for r in riwayat:
            listCatatan.append(r.get_id_catatan())
        text = self.catatan.textEdit.toPlainText()
        for i in range(len(listCatatan)):
            catatan = controllerCatatan(listCatatan[i],text)
            catatan.submitCatatan()
        self.widget.setCurrentWidget(self.home)