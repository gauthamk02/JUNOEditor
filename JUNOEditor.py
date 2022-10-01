import os
import sys
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2

INIT_VAL = 100
MAX_VAL = 100
MIN_VAL = 0

GREEN_IMG = 'ImageSet/JNCE_2022272_45C00002_V01-green.png'
BLUE_IMG = 'ImageSet/JNCE_2022272_45C00002_V01-blue.png'
RED_IMG = 'ImageSet/JNCE_2022272_45C00002_V01-red.png'

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = QLibraryInfo.location(QLibraryInfo.PluginsPath)

class JUNOEditor(QWidget):
    
    def __init__(self, parent = None):
        super(JUNOEditor, self).__init__(parent)

        self.r_val, self.g_val, self.b_val = INIT_VAL, INIT_VAL, INIT_VAL
        self.imageBlue = cv2.imread(BLUE_IMG, 0)
        self.imageGreen = cv2.imread(GREEN_IMG, 0)
        self.imageRed = cv2.imread(RED_IMG, 0)

        self.init_layout()

    def get_image(self):

        b = self.imageBlue.copy()
        g = self.imageGreen.copy()
        r = self.imageRed.copy()
        
        rgb = np.zeros((b.shape[0], b.shape[1], 3), dtype=np.uint8)
        rgb[:, :, 0] = r[:, :] * (self.r_val / 100)
        rgb[:, :, 1] = g[:, :] * (self.g_val / 100)
        rgb[:, :, 2] = b[:, :] * (self.b_val / 100)

        return rgb
        

    def updateImage(self):
        img = self.get_image()
        image = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888)
        self.pic.setPixmap(QPixmap.fromImage(image))
        # print("updateImage")

    def valuechange(self):
        self.r_val = self.sl1.value()
        self.g_val = self.sl2.value()
        self.b_val = self.sl3.value()
        self.l1.setText("Red: " + str(self.r_val))
        self.l2.setText("Green: " + str(self.g_val))
        self.l3.setText("Blue: " + str(self.b_val))
        self.updateImage()

    def init_layout(self):
        layout = QVBoxLayout()

        self.l1 = QLabel("Red: " + str(INIT_VAL))
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)
		
        self.sl1 = QSlider(Qt.Horizontal)
        self.sl1.setMinimum(MIN_VAL)
        self.sl1.setMaximum(MAX_VAL)
        self.sl1.setValue(INIT_VAL)
        self.sl1.valueChanged.connect(self.valuechange)
        layout.addWidget(self.sl1)

        self.l2 = QLabel("Green: " + str(INIT_VAL))
        self.l2.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l2)

        self.sl2 = QSlider(Qt.Horizontal)
        self.sl2.setMinimum(MIN_VAL)
        self.sl2.setMaximum(MAX_VAL)
        self.sl2.setValue(INIT_VAL)
        self.sl2.valueChanged.connect(self.valuechange)
        layout.addWidget(self.sl2)
        
        self.l3 = QLabel("Blue: " + str(INIT_VAL))
        self.l3.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l3)

        self.sl3 = QSlider(Qt.Horizontal)
        self.sl3.setMinimum(MIN_VAL)
        self.sl3.setMaximum(MAX_VAL)
        self.sl3.setValue(INIT_VAL)
        self.sl3.valueChanged.connect(self.valuechange)
        layout.addWidget(self.sl3)

        self.pic = QLabel()
        self.pic.setAlignment(Qt.AlignCenter)
        img = self.get_image()
        image = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888)
        self.pic.setPixmap(QPixmap.fromImage(image))
        layout.addWidget(self.pic)

        self.setLayout(layout)
        self.move(100, 100)
        self.setFixedSize(1000,1000)
        self.setWindowTitle("JUNO Editor")
		
def main():
   app = QApplication(sys.argv)
   screen = JUNOEditor()
   screen.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()