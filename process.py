from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2, imutils
from ImageProcessing import Processing as ip
import numpy as np
import os
from colorCurvePopUp import ColorCurvePopUp

INIT_RGBVAL = 100
MAX_RGBVAL = 100
MIN_RGBVAL = 0

INIT_BRIGHTNESS = 0
MAX_BRIGHTNESS = 100
MIN_BRIGHTNESS = -100

INIT_BLUR = 0
MAX_BLUR = 100
MIN_BLUR = 0

INIT_CONTRAST = 0
MAX_CONTRAST = 100
MIN_CONTRAST = 0

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = QLibraryInfo.location(
    QLibraryInfo.PluginsPath)

class Ui_MainWindow(QWidget):    

    def __init__(self, parent=None):

        super(Ui_MainWindow, self).__init__(parent)

        self.image = cv2.imread("ImageSet/dummyBlack.jpg")
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.image = np.array(self.image)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.initState()
        self.setupUi()
        self.setPhoto(self.image)

    def initState(self):
        self.r_val = INIT_RGBVAL
        self.g_val = INIT_RGBVAL
        self.b_val = INIT_RGBVAL
        self.brightness_value = INIT_BRIGHTNESS
        self.blur_value = INIT_BLUR
        self.contrast_value = INIT_CONTRAST
        self.isEnhanced=False

    def setupUi(self):
        
         # Added code here  
        self.filename = None 
        self.tmp = None 
        self.channels=["RED","GREEN","BLUE"]
        self.selectedChannel="RED"

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1000, 800)

        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # brightness slider
        self.brightnessSlider = QtWidgets.QSlider(self.centralwidget)
        self.brightnessSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brightnessSlider.setObjectName("verticalSlider")
        self.brightnessSlider.setValue(self.brightness_value)
        self.brightnessSlider.setMinimum(MIN_BRIGHTNESS)
        self.brightnessSlider.setMaximum(MAX_BRIGHTNESS)
        self.brightnessLabel = QLabel("Brightness: " + str(self.brightness_value))
        self.brightnessLabel.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.brightnessLabel)
        self.brightnessSlider.valueChanged.connect(self.updateValue)
        self.verticalLayout.addWidget(self.brightnessSlider)
        
        # blur slider
        self.blurSlider = QtWidgets.QSlider(self.centralwidget)
        self.blurSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blurSlider.setObjectName("verticalSlider_2")
        self.blurSlider.setValue(self.blur_value)
        self.blurSlider.setMinimum(MIN_BLUR)
        self.blurSlider.setMaximum(MAX_BLUR)
        self.blurLabel = QLabel("Blur: " + str(self.blur_value))
        self.blurLabel.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.blurLabel)
        self.blurSlider.valueChanged.connect(self.updateValue)
        self.verticalLayout.addWidget(self.blurSlider)

        # contrast slider
        self.contrastSlider = QtWidgets.QSlider(self.centralwidget)
        self.contrastSlider.setOrientation(QtCore.Qt.Horizontal)
        self.contrastSlider.setObjectName("verticalSlider_3")
        self.contrastSlider.setValue(self.contrast_value)
        self.contrastSlider.setMinimum(MIN_CONTRAST)
        self.contrastSlider.setMaximum(MAX_CONTRAST)
        self.contrastLabel = QLabel("Contrast: " + str(self.contrast_value))
        self.contrastLabel.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.contrastLabel)
        self.contrastSlider.valueChanged.connect(self.updateValue)
        self.verticalLayout.addWidget(self.contrastSlider)

        layout = self.verticalLayout
        self.redLabel = QLabel("Red: " + str(INIT_RGBVAL))
        self.redLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.redLabel)

        self.redSlider = QSlider(Qt.Horizontal)
        self.redSlider.setMinimum(MIN_RGBVAL)
        self.redSlider.setMaximum(MAX_RGBVAL)
        self.redSlider.setValue(INIT_RGBVAL)
        self.redSlider.valueChanged.connect(self.valuechange)
        layout.addWidget(self.redSlider)

        self.greenLabel = QLabel("Green: " + str(INIT_RGBVAL))
        self.greenLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.greenLabel)

        self.greenSlider = QSlider(Qt.Horizontal)
        self.greenSlider.setMinimum(MIN_RGBVAL)
        self.greenSlider.setMaximum(MAX_RGBVAL)
        self.greenSlider.setValue(INIT_RGBVAL)
        self.greenSlider.valueChanged.connect(self.valuechange)
        layout.addWidget(self.greenSlider)

        self.blueLabel = QLabel("Blue: " + str(INIT_RGBVAL))
        self.blueLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.blueLabel)

        self.blueSlider = QSlider(Qt.Horizontal)
        self.blueSlider.setMinimum(MIN_RGBVAL)
        self.blueSlider.setMaximum(MAX_RGBVAL)
        self.blueSlider.setValue(INIT_RGBVAL)
        self.blueSlider.valueChanged.connect(self.valuechange)
        layout.addWidget(self.blueSlider)

        # auto-enhance button
        self.autoEnhanceButton = QtWidgets.QPushButton(self.centralwidget)
        self.autoEnhanceButton.setObjectName("autoEnhanceButton")
        self.autoEnhanceButton.setText("Auto Enhance")
        layout.addWidget(self.autoEnhanceButton)
        self.autoEnhanceButton.clicked.connect(self.autoEnhance)

        self.horizontalLayout= QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # dropdown for rgb channel selection
        self.combo_box = QComboBox(self)
        self.combo_box.setObjectName("combo_box")
        self.combo_box.setGeometry(100, 100, 100, 50)
        for channel in self.channels:
            self.combo_box.addItem(channel)
        self.horizontalLayout.addWidget(self.combo_box)
        self.combo_box.activated[int].connect(self.RGBChannelActivated)

        #  button for selecting rgb channel
        self.alterChannelButton = QtWidgets.QPushButton(self.centralwidget)
        self.alterChannelButton.setObjectName("pushButton_3")
        self.alterChannelButton.setText("Alter Channel")
        self.horizontalLayout.addWidget(self.alterChannelButton)
        self.alterChannelButton.clicked.connect(self.takeinputs)

        # --- buttons -------

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # open button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.loadImage)

        
        # save button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.savePhoto)

        # reset button
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_4.clicked.connect(self.resetImage)

  
        # modal called
        self.retranslateUi(MainWindow)

        # image area
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3.setContentsMargins(0,0,0,0)
        # self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("Upload Image")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 4, 1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 0)
        
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
       
        QtCore.QMetaObject.connectSlotsByName(MainWindow)   


    def RGBChannelActivated(self,idx):
        print(self.channels[idx], " Channel Activated")
        self.selectedChannel = self.channels[idx]

    def takeinputs(self):

        msg=QMessageBox()
        msg.setWindowTitle("Input Dialog")
        msg.setText("Color curver value for Red Channel")
        slider=QSlider(Qt.Horizontal)
        msg.addAction(slider)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()        
               
    def autoEnhance(self):
        if(self.isEnhanced == False):
            img = ip.auto_enhance(self.image)
            self.isEnhanced=True
            self.image = img
            self.setPhoto(img)

    def resetSlider(self):
        self.redSlider.setValue(INIT_RGBVAL)
        self.redLabel.setText("Red: " + str(INIT_RGBVAL))
        self.greenSlider.setValue(INIT_RGBVAL)
        self.greenLabel.setText("Green: " + str(INIT_RGBVAL))
        self.blueSlider.setValue(INIT_RGBVAL)
        self.blueLabel.setText("Blue: " + str(INIT_RGBVAL))

        self.contrastSlider.setValue(INIT_CONTRAST)
        self.contrastLabel.setText("Contrast: " + str(INIT_CONTRAST))
        self.brightnessSlider.setValue(INIT_BRIGHTNESS)
        self.brightnessLabel.setText("Brightness: " + str(INIT_BRIGHTNESS))
        self.blurSlider.setValue(INIT_BLUR)
        self.blurLabel.setText("Blur: " + str(INIT_BLUR))

    def resetImage(self):
        self.image = self.origImg
        self.setPhoto(self.image)
        
        self.initState()
        self.resetSlider()

    def updateValue(self):
        self.brightness_value = self.brightnessSlider.value()
        self.blur_value = self.blurSlider.value()
        self.contrast_value = self.contrastSlider.value()

        self.brightnessLabel.setText("Brightness: " + str(self.brightness_value))
        self.blurLabel.setText("Blur: " + str(self.blur_value))
        self.contrastLabel.setText("Contrast: " + str(self.contrast_value))

        self.update()

    def loadImage(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.image = np.array(self.image)
        self.origImg = self.image
        self.initState()
        self.setPhoto(self.image)
    
    def setPhoto(self,image):
        self.tmp = image
        image = imutils.resize(image,width=640)
        image = QImage(image, image.shape[1],image.shape[0],image.strides[0],QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
    
    def update(self):
        brightness = np.interp(self.brightness_value, [-100, 100], [-255, 255]).astype(np.int64)
        img = ip.changeBrightness(self.image, brightness)
        img = ip.changeBlur(img,self.blur_value)
        img = ip.changeContrast(img,self.contrast_value)

        img = ip.channel_correction(img.copy(
        ), (0, 1, 2), (self.r_val / 100, self.g_val / 100, self.b_val / 100))

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
        self.alterChannelButton.setText(_translate("MainWindow", "Alter Channel"))
        self.pushButton_4.setText(_translate("MainWindow", "Reset Image"))
    
    def valuechange(self):
        self.r_val = self.redSlider.value()
        self.g_val = self.greenSlider.value()
        self.b_val = self.blueSlider.value()
        self.redLabel.setText("Red: " + str(self.r_val))
        self.greenLabel.setText("Green: " + str(self.g_val))
        self.blueLabel.setText("Blue: " + str(self.b_val))
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
        QSlider{MainWindow = QtWidgets.QMainWindow()
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
            margin: 10px 5px;
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
        QComboBox{
            color: #fff;
            padding: 10px;
        }
        QComboBox::drop-down {
            
            margin: 6px;
            }
    """
    app.setStyleSheet(style)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())