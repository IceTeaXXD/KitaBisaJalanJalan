import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *

class pilihDestinasiWindow(QDialog):
    def __init__(self):
        super(pilihDestinasiWindow, self).__init__()
        loadUi("./interface/ui/pilihDestinasi.ui", self)

        # create horizontal layout
        self.horizontalLayout = QHBoxLayout(self)
        # set border to transparent
        self.scrollArea = QScrollArea(self)
        # set margin
        self.horizontalLayout.setContentsMargins(100, 250, 100, 300)
        # set background color to transparent
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        
    def setDaerah(self, ListDestinasi):
        for i in range(len(ListDestinasi)):
            self.container = QLabel()
            # set size of container
            self.container.setFixedSize(300, 340)
            # set warna
            self.container.setStyleSheet("background-color: #FFFFFF; border-radius: 10px; padding : 0; margin: 0;")
            decoration = QLabel()
            # set size to 300 x 19
            decoration.setFixedSize(300, 20)
            decoration.setStyleSheet("background-color: #03EF62; border-radius : 10px")
            # make decoration to be top of container with no margin
            decoration.setAlignment(Qt.AlignTop)
            # make a title
            title = QLabel(ListDestinasi[i].getNamaDestinasi())
            # set font size to 20 with font inter
            title.setStyleSheet("font-size: 32px; font-family: Inter; color: #000000;font-weight: 600;")
            # make a checkbox
            checkbox = QCheckBox()
            # set background color to transparent
            checkbox.setStyleSheet("background-color: transparent;")
            # make line 
            line = QFrame()
            line.setFrameShape(QFrame.HLine)
            line.setFrameShadow(QFrame.Sunken)
            line.setStyleSheet("background-color: #000000; margin:10; padding: 0;")
            # set size to 300 x 1
            line.setFixedSize(295, 1)
            # make description
            # set size to 300 x 100
            # desc.setFixedSize(300, 100)
            # make a scroll area
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setFixedHeight(100)
            scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
            scroll_area.setStyleSheet("background-color: transparent;")
            
            desc = QLabel(ListDestinasi[i].getDeskripsi())
            # set font size to 14 with font inter
            desc.setStyleSheet("font-size: 14px; font-family: Inter; color: #000000;")
            # desc.setFixedHeight(100)
            # set margin to 10
            desc.setContentsMargins(10, 10, 10, 10)
            # set alignment to top left
            desc.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            desc.setWordWrap(True)
            desc.setMaximumWidth(300)
            # desc.setFixedSize(300, desc.sizeHint().height())
            scroll_area.setWidget(desc)
            # placeholder image
            img = QLabel()
            imgPath = "../img/lokasiWisata/" + ListDestinasi[i].getGambar()
            img.setPixmap(QPixmap(imgPath))
            img.setContentsMargins(10, 10, 10, 10)
            # make a layout
            self.layout = QVBoxLayout(self.container)
            self.layout.setContentsMargins(0, 0, 0, 0)
            self.layout.addWidget(decoration)
            self.layout.addWidget(title)
            self.layout.addWidget(img)
            self.layout.addWidget(line)
            self.layout.addWidget(scroll_area)
            self.layout.addWidget(checkbox)
            title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
            checkbox.setStyleSheet("margin-left:270; margin-bottom:10")
            # checkbox.setContentsMargins(10,100,100,100)
            decoration.setContentsMargins(0, -10, 0, 0)
            self.gridLayout.addWidget(self.container, 0, i, 1, 1)
    
    def getCheckedVal(self) -> list:
        checked = []
        box_arr = self.scrollAreaWidgetContents.findChildren(QCheckBox, '', Qt.FindChildrenRecursively)
        for i in range(len(box_arr)):
            if (box_arr[i].isChecked()):
                checked.append(i+1)
        return checked
    
    def getNameChecked(self) -> list:
        # get the title of the checked box
        checked = []
        box_arr = self.scrollAreaWidgetContents.findChildren(QCheckBox, '', Qt.FindChildrenRecursively)
        for i in range(len(box_arr)):
            if (box_arr[i].isChecked()):
                checked.append(box_arr[i].parent().findChildren(QLabel, '', Qt.FindChildrenRecursively)[1].text())
        return checked

    def reset(self):
        for i in reversed(range(self.gridLayout.count())): 
            self.gridLayout.itemAt(i).widget().setParent(None)
    
# main function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = pilihDestinasiWindow()
    window.show()
    sys.exit(app.exec_())