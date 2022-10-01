from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2, imutils
from ImageProcessing import Processing as ip
import numpy as np


INIT_VAL = 100
MAX_VAL = 100
MIN_VAL = 0



class Ui_MainWindow(QWidget):    

    def __init__(self, parent=None):

        super(Ui_MainWindow, self).__init__(parent)

        # self.r_val, self.g_val, self.b_val = INIT_VAL, INIT_VAL, INIT_VAL
        # self.imageBlue = cv2.imread(BLUE_IMG, 0)
        # self.imageGreen = cv2.imread(GREEN_IMG, 0)
        # self.imageRed = cv2.imread(RED_IMG, 0)

        # self.img_rgb = np.zeros(
        #         (self.imageBlue.shape[0], self.imageBlue.shape[1], 3), dtype=np.uint8)
        # self.img_rgb[:, :, 0] = self.imageRed[:, :]
        # self.img_rgb[:, :, 1] = self.imageGreen[:, :]
        # self.img_rgb[:, :, 2] = self.imageBlue[:, :]
        self.image=cv2.imread("ImageSet/dummyBlack.jpg", 0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.setupUi()
        self.setPhoto(self.image)
        # self.setupUi()

    def setupUi(self):
        
         # Added code here  
        self.filename = None 
        self.tmp = None # Will hold the temporary image for display
        self.brightness_value_now = 0 # Updated brightness value
        self.brightness_value_now2 = 0 
        self.blur_value_now = 0 # Updated blur value
        self.blur_value_now2 = 0
        self.contrast_value_now = 0 # Updated contrast value
        self.contrast_value_now2 = 0

        self.image=cv2.imread("ImageSet/dummyBlack.jpg", 0)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1000, 800)

        # self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        
        self.horizontalLayout = QtWidgets.QVBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # brightness slider
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider.setValue(self.brightness_value_now2)
        self.l1 = QLabel("Brightness: " + str(self.brightness_value_now2))
        self.l1.setAlignment(Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.l1)
        self.verticalSlider.valueChanged.connect(self.updateValue)
        self.horizontalLayout.addWidget(self.verticalSlider)
        self.verticalSlider.valueChanged['int'].connect(self.brightness_value)
        

        # blur slider
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.l2 = QLabel("Blur: " + str(self.blur_value_now2))
        self.l2.setAlignment(Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.l2)
        self.verticalSlider_2.valueChanged.connect(self.updateValue)
        self.horizontalLayout.addWidget(self.verticalSlider_2)
        self.verticalSlider_2.valueChanged['int'].connect(self.blur_value)

        # contrast slider
        self.verticalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.l3 = QLabel("Contrast: " + str(self.contrast_value_now2))
        self.l3.setAlignment(Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.l3)
        self.verticalSlider_3.valueChanged.connect(self.updateValue)
        self.horizontalLayout.addWidget(self.verticalSlider_3)
        self.verticalSlider_3.valueChanged['int'].connect(self.contrast_value)

        layout = self.horizontalLayout
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

        # --- buttons -------

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # open button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        # save button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)

        # image area
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.setContentsMargins(0,0,0,0)
        # self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("Upload Image")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 4, 1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 0)
        
        
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
       

        self.pushButton_2.clicked.connect(self.loadImage)
        self.pushButton.clicked.connect(self.savePhoto)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
       
    def updateValue(self):
        self.brightness_value_now2 = self.verticalSlider.value()
        self.blur_value_now2 = self.verticalSlider_2.value()
        self.contrast_value_now2 = self.verticalSlider_3.value()

        self.l1.setText("Brightness: " + str(self.brightness_value_now2))
        self.l2.setText("Blur: " + str(self.blur_value_now2))
        self.l3.setText("Contrast: " + str(self.contrast_value_now2))

    def loadImage(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)
    
    def setPhoto(self,image):
        self.tmp = image
        image = imutils.resize(image,width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
    
    def brightness_value(self,value):

        self.brightness_value_now = value
        print('Brightness: ',value)
        self.update()

        
    def blur_value(self,value):

        self.blur_value_now = value
        print('Blur: ',value)
        self.update()

    
    def contrast_value(self,value):
        """ This function will take value from the slider
            for the contrast from 0 to 99
        """
        self.contrast_value_now = value
        print('Contrast: ',value)
        self.update()
    
    
    def changeBrightness(self,img,value):
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(hsv)
        lim = 255 - value
        v[v>lim] = 255
        v[v<=lim] += value
        final_hsv = cv2.merge((h,s,v))
        img = cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
        return img
        
    def changeBlur(self,img,value):
        kernel_size = (value+1,value+1) # +1 is to avoid 0
        img = cv2.blur(img,kernel_size)
        return img

    def changeContrast(self,img,value):

        lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l_channel, a, b = cv2.split(lab)
        # feel free to try different values for the limit and grid size:
        clahe = cv2.createCLAHE(clipLimit=((value/100)+1))
        cl = clahe.apply(l_channel)
        limg = cv2.merge((cl,a,b))
        img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

        # img = np.hstack((img, enhanced_img))
        # hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        # h,s,v = cv2.split(hsv)
        # v[v>127] = 255
        # v[v<=127] += value
        # final_hsv = cv2.merge((h,s,v))
        # img = cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
        return img
    
    def update(self):

        img = self.changeBrightness(self.image,self.brightness_value_now)
        img = self.changeBlur(img,self.blur_value_now)
        img = self.changeContrast(img,self.contrast_value_now)

        img = ip.channel_correction(img.copy(
        ), (0, 1, 2), (self.r_val / 100, self.g_val / 100, self.b_val / 100))
        # print('Image updated')

        self.setPhoto(img)
    
    def savePhoto(self):
        
        filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
        
        cv2.imwrite(filename,self.tmp)
        print('Image saved as:',self.filename)
    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JUNO Photo Editor"))
        self.pushButton_2.setText(_translate("MainWindow", "Open"))
        self.pushButton.setText(_translate("MainWindow", "Save"))

    # RGB Channel Correction
    # def updateImage(self):
    #     img = ip.channel_correction(self.image.copy(
    #     ), (0, 1, 2), (self.r_val / 100, self.g_val / 100, self.b_val / 100))
    #     # img = QImage(img, QImage.Format_RGB888)
    #     # self.pic.setPixmap(QPixmap.fromImage(image))
    #     self.update()
    #     self.setPhoto(img)
        

    
    def valuechange(self):
        self.r_val = self.sl4.value()
        self.g_val = self.sl5.value()
        self.b_val = self.sl6.value()
        self.l4.setText("Red: " + str(self.r_val))
        self.l5.setText("Green: " + str(self.g_val))
        self.l6.setText("Blue: " + str(self.b_val))
        # self.updateImage()
        self.update()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    style = """
        QWidget{
            background: #262D37;
        }
        QLabel{
            color: #fff;
        }
        QSlider{
            height: 8px;
            margin: 15px 0;
        }
        QLabel#round_count_label, QLabel#highscore_count_label{
            border: 1px solid #fff;
            border-radius: 8px;
            padding: 2px;
        }
        QPushButton
        {
            color: white;
            background: #0577a8;
            border: 1px #DADADA solid;
            padding: 10px 15px;
        }
        QPushButton:hover{
            border: 1px #C6C6C6 solid;
            color: #fff;
            background: #0892D0;
        }
        QLineEdit {
            padding: 1px;
            color: #fff;
            border-style: solid;
            border: 2px solid #fff;
            border-radius: 8px;
        }
    """
    app.setStyleSheet(style)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())