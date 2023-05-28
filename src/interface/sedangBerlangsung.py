import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from datetime import datetime
from PyQt5.QtGui import *

from classes.BoundaryRiwayat import *

# arr_sedang_berlangsung = ['Destinasi 1', 'Destinasi 2', 'Destinasi 3', 'Destinasi 4', 'Destinasi 5', 'Destinasi 6', 'Destinasi 7', 'Destinasi 8', 'Destinasi 9', 'Destinasi 10', 'Destinasi 11', 'Destinasi 12', 'Destinasi 13']
class sedangBerlangsungWindow(QDialog):
    def __init__(self):
        super(sedangBerlangsungWindow, self).__init__()
        loadUi("./interface/ui/sedangBerlangsung.ui", self)
        
        # Set the main window size
        self.setFixedSize(1512, 982)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setContentsMargins(200, 250, 180, 140)
        # resize vertical layout
        self.verticalLayout.setSpacing(0)
        
        # Add title label
        tanggal = datetime.today().day
        # bulan -> januari = 1, februari = 2, dst
        bulan = datetime.today().strftime('%B')
        tahun = datetime.today().year
        title = QLabel(str(tanggal) + " " + str(bulan) + " " + str(tahun))
        title.setFixedSize(1132,100)
        title.setStyleSheet("font-size: 35px; font-family: Inter; color: #05192D; font-weight: 600; background-color: #03EF62; border-top-left-radius: 10px; border-top-right-radius: 10px;")
        title.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(title)
        
        # Add scroll area
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        # set color
        self.scrollArea.setStyleSheet("border-bottom-left-radius: 10px; border-bottom-right-radius: 10px; background-color: #FFFFFF;")
        self.scrollArea.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.addWidget(title)
        self.scrollArea.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.scrollArea)
        
        self.setLayout(self.verticalLayout)

    def setSedangBerlangsung(self, data):
        listDestinasi = []
        for riwayat in data:
            list = riwayat.get_list_destinasi()
            for destinasi in list:
                listDestinasi.append((destinasi.getNamaDestinasi(), destinasi.getDeskripsi(), destinasi.getGambar()))
        ulang = len(listDestinasi)//3
        if (len(listDestinasi)%3 != 0):
            ulang += 1
        i = 0
        for row in range(ulang):
            # create a new container for each row
            container = QLabel()
            # container.setStyleSheet("background-color: blue; ")
            container.setFixedSize(1000, 400)
            
            # create a new layout for each container
            container_layout = QHBoxLayout(container)
            container_layout.setContentsMargins(0, 20, 0, 0)
            
            # add elements to the layout
            for j in range(3):
                if i > len(listDestinasi) - 1:
                    break
                element = QLabel()
                element.setFixedSize(300, 300)
                
                decoration = QLabel()
                decoration.setFixedSize(300, 20)
                decoration.setStyleSheet("background-color: #884CFD;")
                label_destinasi = QLabel(listDestinasi[i][0])
                label_destinasi.setFixedSize(300, 200)
                label_destinasi.setStyleSheet("font-size: 20px; font-family: Inter; color: #05192D; font-weight: 600;")

                # placeholder image
                img = QLabel()
                path = "../img/lokasiWisata/" + listDestinasi[i][2]
                img.setPixmap(QPixmap(path))
                img.setContentsMargins(10, 10, 10, 10)

                line = QFrame()
                line.setFrameShape(QFrame.HLine)
                line.setFrameShadow(QFrame.Sunken)
                line.setStyleSheet("background-color: #000000; margin:10; padding: 0;")
                line.setFixedSize(280, 1)

                scroll_area = QScrollArea()
                scroll_area.setWidgetResizable(True)
                scroll_area.setFixedHeight(100)
                scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
                scroll_area.setStyleSheet("background-color: transparent;")

                # make a description label
                desc = QLabel(listDestinasi[i][1])
                desc.setStyleSheet("font-size: 14px; font-family: Inter; color: #05192D; font-weight: 400; border: 0px;")
                desc.setWordWrap(True)
                desc.setMaximumHeight(600)
                desc.setContentsMargins(10, 0, 10, 10)
                scroll_area.setWidget(desc)
                
                element_layout = QVBoxLayout(element)
                element_layout.addWidget(decoration)
                element_layout.addWidget(label_destinasi)
                element_layout.addWidget(img)
                element_layout.addWidget(line)
                element_layout.addWidget(scroll_area)
                element_layout.setContentsMargins(0, 0, 0, 0)
                element_layout.setSpacing(0)
                label_destinasi.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                decoration.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                scroll_area.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
                i += 1

                element.setContentsMargins(0, 0, 0, 0)
                container_layout.addWidget(element)
                decoration.setMargin(0)

            # add the container to the grid layout
            self.gridLayout.addWidget(container, row, 0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = sedangBerlangsungWindow()
    window.show()
    sys.exit(app.exec_())