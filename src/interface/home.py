import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class HomeWindow(QDialog):
    def __init__(self):
        super(HomeWindow, self).__init__()
        loadUi("./interface/ui/home.ui", self)

    def showEvent(self, event): # This is called when the window is shown
        # Animate the frames to slide in
        self.animate_widgets()

    def animate_widgets(self):
        group = QParallelAnimationGroup(self)

        # Animate the text widget
        text_animation = QPropertyAnimation(self.text, b"pos")
        text_animation.setStartValue(QPoint(-self.text.width(), self.text.y()))
        text_animation.setEasingCurve(QEasingCurve.InOutCubic)
        text_animation.setEndValue(QPoint(90,430))
        text_animation.setDuration(1500)
        group.addAnimation(text_animation)

        # Animate the buttons widget
        buttons_animation = QPropertyAnimation(self.buttons, b"pos")
        buttons_animation.setEasingCurve(QEasingCurve.InOutCubic)
        buttons_animation.setStartValue(QPoint(self.width(), 255))  # start from right outside of window
        buttons_animation.setEndValue(QPoint(845, 255))
        buttons_animation.setDuration(1500)
        group.addAnimation(buttons_animation)

        # Start Animating
        group.start()