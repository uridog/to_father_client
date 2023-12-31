# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ready_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMutex


class Ui_readyWindow(object):
    def __init__(self, Client):
        self.client = Client

    def setupUi(self, readyWindow):
        readyWindow.setObjectName("readyWindow")
        readyWindow.resize(800, 600)
        readyWindow.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(readyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self._mutex = QMutex()
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(40, 0, 721, 381))
        self.logo.setObjectName("logo")
        self.voice_button = QtWidgets.QPushButton(self.centralwidget)
        self.voice_button.setGeometry(QtCore.QRect(150, 400, 211, 71))
        self.voice_button.setStyleSheet(";background-color: rgb(162, 47, 255);\n"
                                        "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                        "")
        self.voice_button.setObjectName("voice_button")
        self.waiting_text = QtWidgets.QLabel(self.centralwidget)
        self.waiting_text.setGeometry(QtCore.QRect(140, 480, 481, 41))
        self.waiting_text.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                        "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                        "font-color: rgb(255, 255, 255)")
        self.waiting_text.setObjectName("waiting_text")
        self.waiting_text.hide()
        self.leaderboard_button = QtWidgets.QPushButton(self.centralwidget)
        self.leaderboard_button.setGeometry(QtCore.QRect(370, 400, 251, 71))
        self.leaderboard_button.setStyleSheet(";background-color: rgb(255, 255, 0);\n"
                                              "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;")
        self.leaderboard_button.setObjectName("leaderboard_button")
        self.textgmae_button = QtWidgets.QPushButton(self.centralwidget)
        self.textgmae_button.setGeometry(QtCore.QRect(150, 480, 211, 61))
        self.textgmae_button.setStyleSheet(";background-color: rgb(162, 47, 255);\n"
                                           "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;")
        self.textgmae_button.setObjectName("textgmae_button")
        self.tutorial_button = QtWidgets.QPushButton(self.centralwidget)
        self.tutorial_button.setGeometry(QtCore.QRect(370, 480, 251, 61))
        self.tutorial_button.setStyleSheet(";background-color: rgb(85, 170, 255);\n"
                                           "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;")
        self.tutorial_button.setObjectName("tutorial_button")
        readyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(readyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        readyWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(readyWindow)
        self.statusbar.setObjectName("statusbar")
        readyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(readyWindow)
        QtCore.QMetaObject.connectSlotsByName(readyWindow)
        self.check_for_button(readyWindow)

    def retranslateUi(self, readyWindow):
        _translate = QtCore.QCoreApplication.translate
        readyWindow.setWindowTitle(_translate("readyWindow", "MainWindow"))
        self.logo.setText(
            _translate("readyWindow", "<html><head/><body><p><img src=\":/photos2/logo3.png\"/></p></body></html>"))
        self.voice_button.setText(_translate("readyWindow", "voice-game"))
        self.leaderboard_button.setText(_translate("readyWindow", "leaderboard"))
        self.textgmae_button.setText(_translate("readyWindow", "text-game"))
        self.tutorial_button.setText(_translate("readyWindow", "tutorial"))
        self.waiting_text.setText(_translate("readyWindow",
                                             "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">you are in game</span></p></body></html>"))

    def check_for_button(self, MainWindow):
        self.voice_button.clicked.connect(self.readypressed)
        self.textgmae_button.clicked.connect(self.textpressed)
        self.leaderboard_button.clicked.connect(self.open_leaderboard)
        self.tutorial_button.clicked.connect(self.tutorial_pressed)

    def textpressed(self):
        print("ready pressed")
        self._mutex.lock()
        self.client.voice = False
        self._mutex.unlock()
        self.waiting_text.show()
        self.voice_button.hide()
        self.leaderboard_button.hide()
        self.textgmae_button.hide()
        self.tutorial_button.hide()
        self._mutex.lock()
        self.client.client_ready = True
        self._mutex.unlock()

    def readypressed(self):
        self._mutex.lock()
        self.client.voice = True
        self._mutex.unlock()
        print("ready pressed")
        self.waiting_text.show()
        self.voice_button.hide()
        self.leaderboard_button.hide()
        self.textgmae_button.hide()
        self.tutorial_button.hide()
        self._mutex.lock()
        self.client.client_ready = True
        self._mutex.unlock()

    def open_leaderboard(self):
        self.voice_button.hide()
        self.leaderboard_button.hide()
        self.textgmae_button.hide()
        self.tutorial_button.hide()
        self._mutex.lock()
        self.client.screen_state = 4
        self._mutex.unlock()

    def tutorial_pressed(self):
        self.voice_button.hide()
        self.leaderboard_button.hide()
        self.textgmae_button.hide()
        self.tutorial_button.hide()
        self._mutex.lock()
        self.client.screen_state = 5
        self._mutex.unlock()


def show_lobby_window(window):
    app2 = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    window.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app2.exec_())


import photos2
