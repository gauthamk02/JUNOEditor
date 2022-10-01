import os
import sys
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
from ImageProcessing import Processing as ip

INIT_VAL = 100
MAX_VAL = 100
MIN_VAL = 0

GREEN_IMG = 'ImageSet/JNCE_2022272_45C00002_V01-green.png'
BLUE_IMG = 'ImageSet/JNCE_2022272_45C00002_V01-blue.png'
RED_IMG = 'ImageSet/JNCE_2022272_45C00002_V01-red.png'

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = QLibraryInfo.location(
    QLibraryInfo.PluginsPath)


class JUNOEditor(QWidget):

    
    def __init__(self, parent=None):
        super(JUNOEditor, self).__init__(parent)

        self.r_val, self.g_val, self.b_val = INIT_VAL, INIT_VAL, INIT_VAL
        self.imageBlue = cv2.imread(BLUE_IMG, 0)
        self.imageGreen = cv2.imread(GREEN_IMG, 0)
        self.imageRed = cv2.imread(RED_IMG, 0)

        self.img_rgb = np.zeros(
            (self.imageBlue.shape[0], self.imageBlue.shape[1], 3), dtype=np.uint8)
        self.img_rgb[:, :, 0] = self.imageRed[:, :]
        self.img_rgb[:, :, 1] = self.imageGreen[:, :]
        self.img_rgb[:, :, 2] = self.imageBlue[:, :]

        self.init_layout()


    def updateImage(self):
        img = ip.channel_correction(self.img_rgb.copy(
        ), (0, 1, 2), (self.r_val / 100, self.g_val / 100, self.b_val / 100))
        image = QImage(img, img.shape[1], img.shape[0],
                       img.strides[0], QImage.Format_RGB888)
        self.pic.setPixmap(QPixmap.fromImage(image))

    
    def valuechange(self):
        self.r_val = self.sl4.value()
        self.g_val = self.sl5.value()
        self.b_val = self.sl6.value()
        self.l4.setText("Red: " + str(self.r_val))
        self.l5.setText("Green: " + str(self.g_val))
        self.l6.setText("Blue: " + str(self.b_val))
        self.updateImage()

    
    def init_layout(self):
        layout = QVBoxLayout()

        self.l4 = QLabel("Red: " + str(INIT_VAL))
        self.l4.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l4)

        self.sl4 = QSlider(Qt.Horizontal)
        self.sl4.setMinimum(MIN_VAL)
        self.sl4.setMaximum(MAX_VAL)
        self.sl4.setValue(INIT_VAL)
        self.sl4.valueChanged.connect(self.valuechange)
        layout.addWidget(self.sl4)

        self.l5 = QLabel("Green: " + str(INIT_VAL))
        self.l5.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l5)

        self.sl5 = QSlider(Qt.Horizontal)
        self.sl5.setMinimum(MIN_VAL)
        self.sl5.setMaximum(MAX_VAL)
        self.sl5.setValue(INIT_VAL)
        self.sl5.valueChanged.connect(self.valuechange)
        layout.addWidget(self.sl5)

        self.l6 = QLabel("Blue: " + str(INIT_VAL))
        self.l6.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l6)

        self.sl6 = QSlider(Qt.Horizontal)
        self.sl6.setMinimum(MIN_VAL)
        self.sl6.setMaximum(MAX_VAL)
        self.sl6.setValue(INIT_VAL)
        self.sl6.valueChanged.connect(self.valuechange)
        layout.addWidget(self.sl6)

        self.pic = QLabel()
        self.pic.setAlignment(Qt.AlignCenter)
        image = QImage(
            self.img_rgb, self.img_rgb.shape[1], self.img_rgb.shape[0], self.img_rgb.strides[0], QImage.Format_RGB888)
        self.pic.setPixmap(QPixmap.fromImage(image))
        layout.addWidget(self.pic)

        self.setLayout(layout)
        self.move(100, 100)
        self.setFixedSize(1000, 1000)
        self.setWindowTitle("JUNO Editor")


def main():
    app = QApplication(sys.argv)
    style = """
   """
    screen = JUNOEditor()
    screen.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
