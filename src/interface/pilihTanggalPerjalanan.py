import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class pilihTanggalPerjalananWindow(QDialog):
    def __init__(self):
        super(pilihTanggalPerjalananWindow, self).__init__()
        loadUi("./interface/ui/pilihTanggalPerjalanan.ui", self)

        self.from_date = self.calendarWidget.selectedDate()
        self.to_date = None

        self.highlighter = QTextCharFormat()
        self.highlighter.setBackground(self.palette().brush(QPalette.Highlight))
        self.highlighter.setForeground(self.palette().brush(QPalette.HighlightedText))

        self.calendarWidget.clicked.connect(self.select_date_range)

    def select_date_range(self, date_value):
        self.highlight_range(QTextCharFormat())

        if QApplication.instance().keyboardModifiers() & Qt.ShiftModifier and self.from_date:
            self.to_date = date_value
            self.highlight_range(self.highlighter)
        else:
            self.from_date = date_value
            self.to_date = None
    
    def highlight_range(self,format):
        if self.from_date and self.to_date:
            d1 = min(self.from_date, self.to_date)
            d2 = max(self.from_date, self.to_date)
            while d2>= d1:
                self.calendarWidget.setDateTextFormat(d1, format)
                d1 = d1.addDays(1)

    def getDateSelected(self):
        # return the selected date in DD/MM/YYYY format
        if self.from_date and self.to_date:
            return self.from_date.toString("yyyy-MM-dd"), self.to_date.toString("yyyy-MM-dd")
        else:
            return self.from_date.toString("yyyy-MM-dd"), None