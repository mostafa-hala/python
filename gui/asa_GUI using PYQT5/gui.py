# A pdf containing task delegation along with the controls for the gui is found in the repo

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from string import Template
from multiprocessing.connection import Listener, Client
from threading import Thread, current_thread
import time
import cv2, numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.minutes = 0
        self.seconds = 0
        self.counter = 0
        self.flag = False
        self.display_width = 461
        self.display_height = 361

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1246, 875)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1381, 841))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("a.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 10, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(
            QtCore.QRect(10, 60, self.display_width, self.display_height)
        )
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(
            QtCore.QRect(770, 60, self.display_width, self.display_height)
        )
        self.label_4.setObjectName("label_4")
        self.vehicleIndicators = QtWidgets.QGroupBox(self.centralwidget)
        self.vehicleIndicators.setGeometry(QtCore.QRect(9, 459, 571, 361))
        self.vehicleIndicators.setObjectName("vehicleIndicators")
        self.label_5 = QtWidgets.QLabel(self.vehicleIndicators)
        self.label_5.setGeometry(QtCore.QRect(10, -11, 91, 31))
        self.label_5.setObjectName("label_5")
        self.groupBox = QtWidgets.QGroupBox(self.vehicleIndicators)
        self.groupBox.setGeometry(QtCore.QRect(30, 40, 161, 151))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(0, 10, 161, 131))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("grapper-close.png"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.vehicleIndicators)
        self.groupBox_2.setGeometry(QtCore.QRect(190, 40, 161, 151))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(6, 2, 151, 141))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("grapper-close-horizontalpng.png"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.groupBox_3 = QtWidgets.QGroupBox(self.vehicleIndicators)
        self.groupBox_3.setGeometry(QtCore.QRect(350, 40, 161, 151))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_7)
        self.label_8.setGeometry(QtCore.QRect(10, -1, 91, 31))
        self.label_8.setObjectName("label_8")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_8.setGeometry(QtCore.QRect(9, 50, 141, 31))
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_8)
        self.label_9.setGeometry(QtCore.QRect(10, 0, 101, 31))
        self.label_9.setObjectName("label_9")
        self.groupBox_4 = QtWidgets.QGroupBox(self.vehicleIndicators)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 190, 161, 161))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(50, 10, 61, 41))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("frwrd-arrowred.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(10, 50, 41, 61))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("left-arrowred.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(50, 110, 61, 41))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("bckwrd-arrowred.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(110, 50, 41, 61))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("right-arrowred.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.groupBox_5 = QtWidgets.QGroupBox(self.vehicleIndicators)
        self.groupBox_5.setGeometry(QtCore.QRect(190, 190, 161, 161))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 151, 61))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("cwred.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(10, 80, 151, 61))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("ccwred.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.groupBox_6 = QtWidgets.QGroupBox(self.vehicleIndicators)
        self.groupBox_6.setGeometry(QtCore.QRect(350, 190, 161, 161))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_16 = QtWidgets.QLabel(self.groupBox_6)
        self.label_16.setGeometry(QtCore.QRect(40, 20, 71, 61))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("upward-arrowred.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_6)
        self.label_17.setGeometry(QtCore.QRect(40, 90, 71, 61))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("downward-arrowred.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(590, 460, 341, 121))
        self.groupBox_9.setObjectName("groupBox_9")
        self.label_18 = QtWidgets.QLabel(self.groupBox_9)
        self.label_18.setGeometry(QtCore.QRect(10, -10, 91, 31))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_9)
        self.label_19.setGeometry(QtCore.QRect(0, 20, 321, 31))
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.pushButton = QtWidgets.QPushButton(
            self.groupBox_9, clicked=lambda: self.start()
        )
        self.pushButton.setGeometry(QtCore.QRect(10, 80, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(
            self.groupBox_9, clicked=lambda: self.stop()
        )
        self.pushButton_2.setGeometry(QtCore.QRect(120, 80, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(
            self.groupBox_9, clicked=lambda: self.reset()
        )
        self.pushButton_3.setGeometry(QtCore.QRect(230, 80, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(590, 590, 341, 231))
        self.groupBox_10.setObjectName("groupBox_10")
        self.label_20 = QtWidgets.QLabel(self.groupBox_10)
        self.label_20.setGeometry(QtCore.QRect(10, -10, 91, 31))
        self.label_20.setObjectName("label_20")
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_11.setGeometry(QtCore.QRect(20, 30, 141, 31))
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")
        self.label_21 = QtWidgets.QLabel(self.groupBox_11)
        self.label_21.setGeometry(QtCore.QRect(10, 0, 101, 31))
        self.label_21.setObjectName("label_21")
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_12.setGeometry(QtCore.QRect(20, 70, 141, 31))
        self.groupBox_12.setTitle("")
        self.groupBox_12.setObjectName("groupBox_12")
        self.label_22 = QtWidgets.QLabel(self.groupBox_12)
        self.label_22.setGeometry(QtCore.QRect(10, 0, 101, 31))
        self.label_22.setObjectName("label_22")
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_13.setGeometry(QtCore.QRect(20, 110, 141, 31))
        self.groupBox_13.setTitle("")
        self.groupBox_13.setObjectName("groupBox_13")
        self.label_23 = QtWidgets.QLabel(self.groupBox_13)
        self.label_23.setGeometry(QtCore.QRect(10, 0, 101, 31))
        self.label_23.setObjectName("label_23")
        self.groupBox_14 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_14.setGeometry(QtCore.QRect(20, 150, 141, 31))
        self.groupBox_14.setTitle("")
        self.groupBox_14.setObjectName("groupBox_14")
        self.label_24 = QtWidgets.QLabel(self.groupBox_14)
        self.label_24.setGeometry(QtCore.QRect(10, 0, 101, 31))
        self.label_24.setObjectName("label_24")
        self.groupBox_15 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_15.setGeometry(QtCore.QRect(940, 460, 291, 121))
        self.groupBox_15.setObjectName("groupBox_15")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_15)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 121, 31))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_4 = QtWidgets.QPushButton(
            self.groupBox_15, clicked=lambda: self.comboboxChoice()
        )
        self.pushButton_4.setGeometry(QtCore.QRect(160, 50, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(950, 450, 91, 31))
        self.label_25.setObjectName("label_25")
        self.groupBox_16 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_16.setGeometry(QtCore.QRect(940, 590, 291, 231))
        self.groupBox_16.setObjectName("groupBox_16")
        self.label_27 = QtWidgets.QLabel(self.groupBox_16)
        self.label_27.setGeometry(QtCore.QRect(10, 30, 200, 31))
        self.label_27.setObjectName("label_27")
        self.pushButton_5 = QtWidgets.QPushButton(
            self.groupBox_16, clicked=lambda: self.autonomous()
        )
        self.pushButton_5.setGeometry(QtCore.QRect(10, 70, 101, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(
            self.groupBox_16, clicked=lambda: self.depthHold()
        )
        self.pushButton_6.setGeometry(QtCore.QRect(10, 110, 101, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(
            self.groupBox_16, clicked=lambda: self.stabilize()
        )
        self.pushButton_7.setGeometry(QtCore.QRect(10, 150, 101, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(
            self.groupBox_16, clicked=lambda: self.manual()
        )
        self.pushButton_8.setGeometry(QtCore.QRect(10, 190, 101, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(950, 580, 91, 31))
        self.label_26.setObjectName("label_26")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1246, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Adding items to the comboBox
        self.comboBox.addItem("Code 1")
        self.comboBox.addItem("Code 2")
        self.comboBox.addItem("Code 3")

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(100)

    # Dummy functions to test which element in combobox is chosen
    def code1(self):
        print("Code 1 is executing")

    def code2(self):
        print("Code 2 is executing")

    def code3(self):
        print("Code 3 is executing")

    # Function to act according to combobox choice and at the button click it can be replaced with any other script
    def comboboxChoice(self):
        choice = self.comboBox.currentText()
        if choice == "Code 1":
            self.code1()
        elif choice == "Code 2":
            self.code2()
        elif choice == "Code 3":
            self.code3()

    def autonomous(self):
        self.label_27.setText(
            '<html><head/><body><p><span style=" font-size:12pt; color:#ffffff;">Current mode: Autonomous</span></p></body></html>'
        )

    def depthHold(self):
        self.label_27.setText(
            '<html><head/><body><p><span style=" font-size:12pt; color:#ffffff;">Current mode: Depth Hold</span></p></body></html>'
        )

    def stabilize(self):
        self.label_27.setText(
            '<html><head/><body><p><span style=" font-size:12pt; color:#ffffff;">Current mode: Stabilize</span></p></body></html>'
        )

    def manual(self):
        self.label_27.setText(
            '<html><head/><body><p><span style=" font-size:12pt; color:#ffffff;">Current mode: Manual</span></p></body></html>'
        )

    def start(self):
        self.flag = True  # Sets flag to true to make timer run

    def stop(self):
        self.flag = False

    def reset(self):
        self.flag = False
        self.counter = 0
        self.seconds = 0
        self.label_19.setText(
            str(
                '<html><head/><body><p><span style=" font-size:18pt; color:#ffffff;">0:0</span></p></body></html>'
            )
        )

    def showTime(self):
        if self.flag:
            self.counter += 1
        text = str(self.counter % 10)
        if text == "0" and self.flag:
            self.seconds += 1
        seconds = str(self.seconds)
        if seconds == "60" and self.flag:
            self.minutes += 1
            self.seconds = 0
        minutes = str(self.minutes)

        self.label_19.setText(
            f'<html><head/><body><p><span style=" font-size:18pt; color:#ffffff;">{minutes}:{seconds}:{text}</span></p></body></html>'
        )

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:24pt; color:#ffffff;">Vortex GUI</span></p></body></html>',
            )
        )
        self.label_3.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">Camera 1</span></p></body></html>',
            )
        )
        self.label_4.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; color:#ffffff;">Camera 2</span></p></body></html>',
            )
        )
        self.vehicleIndicators.setTitle(
            _translate("MainWindow", "                             ")
        )
        self.label_5.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">Vehicle Indicators</span></p></body></html>',
            )
        )
        self.label_8.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; color:#ffffff;">Current speed:</span></p></body></html>',
            )
        )
        self.label_9.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; color:#ffffff;">Current heading:</span></p></body></html>',
            )
        )
        self.groupBox_9.setTitle(_translate("MainWindow", "         "))
        self.label_18.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">Timer</span></p></body></html>',
            )
        )
        self.label_19.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:18pt; color:#ffffff;">00:00:00</span></p></body></html>',
            )
        )
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))
        self.pushButton_3.setText(_translate("MainWindow", "Reset"))
        self.groupBox_10.setTitle(
            _translate("MainWindow", "                           ")
        )
        self.label_20.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">Sensor Readings</span></p></body></html>',
            )
        )
        self.label_21.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; color:#ffffff;">Depth:</span></p></body></html>',
            )
        )
        self.label_22.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; color:#ffffff;">X acc:</span></p></body></html>',
            )
        )
        self.label_23.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; color:#ffffff;">Y acc:</span></p></body></html>',
            )
        )
        self.label_24.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; color:#ffffff;">Z acc:</span></p></body></html>',
            )
        )
        self.groupBox_15.setTitle(_translate("MainWindow", "           "))
        self.pushButton_4.setText(_translate("MainWindow", "Run"))
        self.label_25.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">Scripts</span></p></body></html>',
            )
        )
        self.groupBox_16.setTitle(_translate("MainWindow", "                      "))
        self.label_27.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; color:#ffffff;">Current mode:</span></p></body></html>',
            )
        )
        self.pushButton_5.setText(_translate("MainWindow", "Autonomous"))
        self.pushButton_6.setText(_translate("MainWindow", "Depth hold"))
        self.pushButton_7.setText(_translate("MainWindow", "Stabilize"))
        self.pushButton_8.setText(_translate("MainWindow", "Manual"))
        self.label_26.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">Current mode</span></p></body></html>',
            )
        )

    def transmit1():
        try:
            address = ("localhost", 6001)
            conn = Client(address, authkey=b"secret password")
            # MAX RESOLUTION
            frame_width = MAX_WIDTH = 1280
            frame_height = MAX_HEIGHT = 720

            # try to set max resolution
            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

            # get max resolution
            frame_width = int(cap.get(3))
            frame_height = int(cap.get(4))
            success, original_frame = cap.read()
            while success:
                conn.send(original_frame)
                success, original_frame = cap.read()
            conn.send("close")
            conn.close()
        except Exception as e:
            print(e)

    def receive1(self):
        try:
            address = ("localhost", 6001)  # family is deduced to be 'AF_INET'
            listener = Listener(address, authkey=b"secret password")
            conn = listener.accept()
            cv_img = conn.recv()
            while type(cv_img) is not str:
                rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                p = QtGui.QImage(
                    rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888
                )
                p = QPixmap.fromImage(p).scaled(
                    self.display_width, self.display_height, Qt.KeepAspectRatio
                )
                self.label_3.setPixmap(p)
                cv_img = conn.recv()
            listener.close()
        except Exception as e:
            print(e)

    def transmit2():
        try:
            address = ("localhost", 6002)
            conn = Client(address, authkey=b"secret password")
            # MAX RESOLUTION
            frame_width = MAX_WIDTH = 1280
            frame_height = MAX_HEIGHT = 720

            # try to set max resolution
            cap = cv2.VideoCapture(1)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

            # get max resolution
            frame_width = int(cap.get(3))
            frame_height = int(cap.get(4))
            success, original_frame = cap.read()
            while success:
                conn.send(original_frame)
                success, original_frame = cap.read()
            conn.send("close")
            conn.close()
        except Exception as e:
            print(e)

    def receive2(self):
        try:
            address = ("localhost", 6002)  # family is deduced to be 'AF_INET'
            listener = Listener(address, authkey=b"secret password")
            conn = listener.accept()
            cv_img = conn.recv()
            while type(cv_img) is not str:
                rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                p = QtGui.QImage(
                    rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888
                )
                p = QPixmap.fromImage(p).scaled(
                    self.display_width, self.display_height, Qt.KeepAspectRatio
                )
                self.label_4.setPixmap(p)
                cv_img = conn.recv()

            listener.close()
        except Exception as e:
            print(e)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            self.label_10.setPixmap(QtGui.QPixmap("frwrd-arrow.png"))
        elif event.key() == Qt.Key_S:
            self.label_12.setPixmap(QtGui.QPixmap("bckwrd-arrow.png"))
        elif event.key() == Qt.Key_A:
            self.label_11.setPixmap(QtGui.QPixmap("left-arrow.png"))
        elif event.key() == Qt.Key_D:
            self.label_13.setPixmap(QtGui.QPixmap("right-arrow.png"))
        elif event.key() == Qt.Key_I:
            self.label_16.setPixmap(QtGui.QPixmap("upward-arrow.png"))
        elif event.key() == Qt.Key_K:
            self.label_17.setPixmap(QtGui.QPixmap("downward-arrow.png"))
        elif event.key() == Qt.Key_Q:
            self.label_15.setPixmap(QtGui.QPixmap("ccw.png"))
        elif event.key() == Qt.Key_E:
            self.label_14.setPixmap(QtGui.QPixmap("cw.png"))
        elif event.key() == Qt.Key_J:
            self.label_6.setPixmap(QtGui.QPixmap("grapper-open.png"))
        elif event.key() == Qt.Key_L:
            self.label_7.setPixmap(QtGui.QPixmap("grapper-open-horizontal.png"))

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_W:
            self.label_10.setPixmap(QtGui.QPixmap("frwrd-arrowred.png"))
        elif event.key() == Qt.Key_S:
            self.label_12.setPixmap(QtGui.QPixmap("bckwrd-arrowred.png"))
        elif event.key() == Qt.Key_A:
            self.label_11.setPixmap(QtGui.QPixmap("left-arrowred.png"))
        elif event.key() == Qt.Key_D:
            self.label_13.setPixmap(QtGui.QPixmap("right-arrowred.png"))
        elif event.key() == Qt.Key_I:
            self.label_16.setPixmap(QtGui.QPixmap("upward-arrowred.png"))
        elif event.key() == Qt.Key_K:
            self.label_17.setPixmap(QtGui.QPixmap("downward-arrowred.png"))
        elif event.key() == Qt.Key_Q:
            self.label_15.setPixmap(QtGui.QPixmap("ccwred.png"))
        elif event.key() == Qt.Key_E:
            self.label_14.setPixmap(QtGui.QPixmap("cwred.png"))
        elif event.key() == Qt.Key_J:
            self.label_6.setPixmap(QtGui.QPixmap("grapper-close.png"))
        elif event.key() == Qt.Key_L:
            self.label_7.setPixmap(QtGui.QPixmap("grapper-close-horizontalpng.png"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()

    t1 = Thread(target=Ui_MainWindow.transmit1)
    t1.daemon = True
    t1.start()

    t2 = Thread(target=w.receive1)
    t2.daemon = True
    t2.start()

    t3 = Thread(target=Ui_MainWindow.transmit2)
    t3.daemon = True
    t3.start()

    t4 = Thread(target=w.receive2)
    t4.daemon = True
    t4.start()

    sys.exit(app.exec_())
