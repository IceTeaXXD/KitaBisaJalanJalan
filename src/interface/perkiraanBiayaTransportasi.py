import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap

from classes.ListTransportasi import *

arrray_of_destiansi = [['Destinasi 1',10000,20000,30000,40000],['Destinasi 2',16000,20000,30000,40000],['Destinasi 3',10090,20000,30000,40000]]
class PerkiraanBiayaTransportasiWindow(QDialog):
    def __init__(self):
        super(PerkiraanBiayaTransportasiWindow, self).__init__()
        loadUi("./interface/ui/perkiraanBiayaTransportasi.ui", self)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setContentsMargins(100, 250, 100, 300)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)
        self.setLayout(self.verticalLayout)

        self.listTransportasi = ListTransportasi().getList()
        
    def setDestinasi(self, ListDestinasiPilihan):
        for i in range(len(ListDestinasiPilihan)):
            self.container = QLabel()
            self.container.setFixedSize(1200, 400)
            self.container.setStyleSheet("background-color: transparent; border-radius: 10px; margin-bottom : 20px")

            box = QHBoxLayout(self.container)
            box.setContentsMargins(0, 0, 0, 0)
            box.setSpacing(40)

            # box di kiri
            left_box = QLabel()
            left_box.setFixedSize(400, 400)
            left_box.setStyleSheet("background-color: #F2F2F2; border-radius: 10px;")

            decoration = QLabel()
            decoration.setFixedSize(400, 40)
            decoration.setStyleSheet("background-color: #03EF62; border-radius: 10px;")

            title = QLabel(ListDestinasiPilihan[i].getNamaDestinasi())
            title.setStyleSheet("color: #000000; font-size: 32px; font-weight: bold;")

            line = QFrame()
            line.setFrameShape(QFrame.HLine)
            line.setFrameShadow(QFrame.Sunken)
            line.setStyleSheet("background-color: #000000; margin:10; padding: 0;")
            line.setFixedSize(380, 1)

            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setFixedHeight(100)
            scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
            scroll_area.setStyleSheet("background-color: transparent;")

            desc = QLabel(ListDestinasiPilihan[i].getDeskripsi())
            desc.setStyleSheet("color: #000000; font-size: 16px;")
            desc.setWordWrap(True)
            desc.setMaximumHeight(600)
            desc.setContentsMargins(10, 0, 10, 10)
            scroll_area.setWidget(desc)

            # add placeholder image
            img = QLabel()
            path = "../img/lokasiWisata/" + ListDestinasiPilihan[i].getGambar()
            img.setPixmap(QPixmap(path))
            img.setContentsMargins(10, 10, 10, 10)

            left_box_layout = QVBoxLayout(left_box)
            left_box_layout.addWidget(decoration)
            left_box_layout.addWidget(title)
            left_box_layout.addWidget(img)
            left_box_layout.addWidget(line)
            left_box_layout.addWidget(scroll_area)
            left_box_layout.setContentsMargins(0, 0, 0, 0)

            box.addWidget(left_box)
            decoration.setAlignment(Qt.AlignTop)
            title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
            line.setContentsMargins(0, 0, 0, 0)
            desc.setAlignment(Qt.AlignTop | Qt.AlignLeft)

            decoration.setMargin(0)
            right_box = QLabel()
            right_box.setFixedSize(800, 400)
            right_box.setStyleSheet("background-color: #F2F2F2; border-radius: 10px;")
            right_box.setAlignment(Qt.AlignCenter)
            right_box_layout = QHBoxLayout(right_box)
            right_box_layout.setContentsMargins(0, 0, 0, 0)
            right_box_layout.setSpacing(0)
            right_box.setAlignment(Qt.AlignCenter)

            # radio button container
            radio_container = QLabel()
            radio_container.setFixedWidth(80)
            
            # make a radio button
            radio_kereta = QRadioButton(str(self.listTransportasi[0].getHarga()))
            radio_kereta.setStyleSheet("color: transparent")
            radio_pesawat = QRadioButton(str(self.listTransportasi[1].getHarga()))
            radio_pesawat.setStyleSheet("color: transparent")
            radio_mobil = QRadioButton(str(self.listTransportasi[2].getHarga()))
            radio_mobil.setStyleSheet("color: transparent")
            radio_bus = QRadioButton(str(self.listTransportasi[3].getHarga()))
            radio_bus.setStyleSheet("color: transparent")

            # make a group
            group = QButtonGroup()
            group.addButton(radio_kereta)
            group.addButton(radio_pesawat)
            group.addButton(radio_mobil)
            group.addButton(radio_bus)

            radio_container_layout = QVBoxLayout(radio_container)
            radio_container_layout.addWidget(radio_kereta)
            radio_container_layout.addWidget(radio_pesawat)
            radio_container_layout.addWidget(radio_mobil)
            radio_container_layout.addWidget(radio_bus)

            radio_container_layout.setContentsMargins(30, 35, 0, 0)
            radio_container_layout.setSpacing(60)
            right_box_layout.addWidget(radio_container)

            # make an image container
            img_container = QLabel()
            img_container.setFixedWidth(100)
            img_container.setStyleSheet("margin : 0")

            img_pesawat = QLabel()
            img_pesawat.setPixmap(QPixmap("../img/biayaTransport/Plane.png"))
            img_kereta = QLabel()
            img_kereta.setPixmap(QPixmap("../img/biayaTransport/Train.png"))
            img_mobil = QLabel()
            img_mobil.setPixmap(QPixmap("../img/biayaTransport/People in Car.png"))
            img_bus = QLabel()
            img_bus.setPixmap(QPixmap("../img/biayaTransport/Bus.png"))

            img_container_layout = QVBoxLayout(img_container)
            img_container_layout.addWidget(img_kereta)
            img_container_layout.addWidget(img_pesawat)
            img_container_layout.addWidget(img_mobil)
            img_container_layout.addWidget(img_bus)
            img_container_layout.setAlignment(Qt.AlignLeft)

            img_container_layout.setContentsMargins(0, 0, 0, 0)
            img_container_layout.setSpacing(20)
            right_box_layout.addWidget(img_container)

            # make a label container
            label_container = QLabel()
            label_container_layout = QVBoxLayout(label_container)
            label_container_layout.setContentsMargins(0, 0, 0, 0)
            label_container_layout.setSpacing(20)
            
            # make a label
            label_mobil = QLabel("Tiket Mobil Rp. " + str(self.listTransportasi[2].getHarga()))
            label_mobil.setStyleSheet("color: #000000; font-size: 32px; font-weight: bold; margin-bottom : 20px; margin-top : 20px; ")
            label_bus = QLabel("Tiket Bus Rp. " + str(self.listTransportasi[3].getHarga()))
            label_bus.setStyleSheet("color: #000000; font-size: 32px; font-weight: bold; margin-bottom : 20px; margin-top : 20px; ")
            label_kereta = QLabel("Tiket Kereta Rp. " + str(self.listTransportasi[0].getHarga()))
            label_kereta.setStyleSheet("color: #000000; font-size: 32px; font-weight: bold; margin-bottom : 20px; margin-top : 20px; ")
            label_pesawat = QLabel("Tiket Pesawat Rp. " + str(self.listTransportasi[1].getHarga()))
            label_pesawat.setStyleSheet("color: #000000; font-size: 32px; font-weight: bold; margin-bottom : 20px; margin-top : 20px; ")

            label_container_layout.addWidget(label_kereta)
            label_container_layout.addWidget(label_pesawat)
            label_container_layout.addWidget(label_mobil)
            label_container_layout.addWidget(label_bus)
            label_container_layout.setAlignment(Qt.AlignLeft)
            right_box_layout.addWidget(label_container)
            right_box_layout.setSpacing(0)
            right_box_layout.setContentsMargins(0, 0, 0, 0)
            box.addWidget(right_box)

            self.gridLayout.addWidget(self.container, i, 0, 1, 1)

    def reset(self):
        for i in reversed(range(self.gridLayout.count())): 
            self.gridLayout.itemAt(i).widget().setParent(None)

    def checkedTransportasiHarga(self):
        checked = []
        box_arr = self.scrollAreaWidgetContents.findChildren(QRadioButton, '', Qt.FindChildrenRecursively)
        # get the checked button text

        for i in range(len(box_arr)):
            if box_arr[i].isChecked():
                checked.append(((i % 4) + 1,box_arr[i].text()))

        return checked


                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PerkiraanBiayaTransportasiWindow()
    window.show()
    sys.exit(app.exec_())