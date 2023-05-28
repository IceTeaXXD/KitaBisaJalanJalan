import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

from classes.BoundaryRiwayat import *

class riwayatPerjalananWindow(QDialog):
    def __init__(self):
        super(riwayatPerjalananWindow, self).__init__()
        loadUi("./interface/ui/riwayatPerjalanan.ui", self)
        self.selectDate = None

    def getDateSelected(self):
        return self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
    
    def getRiwayat(self):
        riwayat = BoundaryRiwayat()
        self.selectDate = self.getDateSelected()
        return riwayat.getRiwayat(tgl = self.getDateSelected())