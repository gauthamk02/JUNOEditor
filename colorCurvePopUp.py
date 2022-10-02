from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ColorCurvePopUp(QToolButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setIcon(volumeicon)

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setFixedSize(100, 20)
        
        # self.slider.setWindowFlags(Qt.FramelessWindowHint)
        # self.slider.setWindowModality(Qt.NonModal)
        # self.slider.installEventFilter(self)

    # def isInside(self):
    #     buttonRect = self.rect().translated(self.mapToGlobal(QPoint()))
    #     if not self.slider.isVisible():
    #         return QCursor.pos() in buttonRect
    #     region = QRegion(buttonRect)
    #     region |= QRegion(self.slider.geometry())
    #     return region.contains(QCursor.pos())

    # def enterEvent(self, event):
    #     if not self.slider.isVisible():
    #         self.slider.move(self.mapToGlobal(QPoint()))
    #         self.slider.show()

    # def leaveEvent(self, event):
    #     if not self.isInside():
    #         self.slider.hide()

    # def eventFilter(self, source, event):
    #     if source == self.slider and event.type() == event.Leave:
    #         if not self.isInside():
    #             self.slider.hide()
    #     return super().eventFilter(source, event)



    def __init__(self, curveColor,parent):
        super().__init__(parent)
        MainWindow = QtWidgets.QMainWindow()
        self.resize(600,300)
        self.popUp(curveColor,MainWindow)
       

    def popUp(self,curveColor,MainWindow):
        print(curveColor)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider.setValue(0)
        self.verticalSlider.setMinimum(-100)
        self.verticalSlider.setMaximum(100)
        self.verticalLayout.addWidget(self.verticalSlider)
