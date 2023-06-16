# -*- coding: utf-8 -*-
import sys

# Form implementation generated from reading ui file 'leadrboard_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMutex


class Ui_MainWindow(object):
    def __init__(self, Client):
        self.client = Client

    def setupUi(self, MainWindow, user_list, curr_user):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self._mutex = QMutex()
        self.leaderboard_title = QtWidgets.QLabel(self.centralwidget)
        self.leaderboard_title.setGeometry(QtCore.QRect(160, 40, 461, 81))
        self.leaderboard_title.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                             "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                             "")
        self.leaderboard_title.setObjectName("leaderboard_title")
        self.first_place = QtWidgets.QLabel(self.centralwidget)
        self.first_place.setGeometry(QtCore.QRect(60, 170, 31, 71))
        self.first_place.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                       "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                       "")
        self.first_place.setObjectName("first_place")
        self.second_place = QtWidgets.QLabel(self.centralwidget)
        self.second_place.setGeometry(QtCore.QRect(56, 260, 41, 51))
        self.second_place.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                        "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                        "")
        self.second_place.setObjectName("second_place")
        self.third_place = QtWidgets.QLabel(self.centralwidget)
        self.third_place.setGeometry(QtCore.QRect(50, 330, 41, 41))
        self.third_place.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                       "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                       "")
        self.third_place.setObjectName("third_place")
        self.first_place_name = QtWidgets.QLabel(self.centralwidget)
        self.first_place_name.setGeometry(QtCore.QRect(110, 170, 541, 61))
        self.first_place_name.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                            "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                            "")
        self.first_place_name.setObjectName("first_place_name")
        self.second_place_name = QtWidgets.QLabel(self.centralwidget)
        self.second_place_name.setGeometry(QtCore.QRect(110, 250, 541, 61))
        self.second_place_name.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                             "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                             "")
        self.second_place_name.setObjectName("second_place_name")
        self.third_place_name = QtWidgets.QLabel(self.centralwidget)
        self.third_place_name.setGeometry(QtCore.QRect(110, 330, 541, 51))
        self.third_place_name.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                            "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                            "")
        self.third_place_name.setObjectName("third_place_name")
        self.user_place = QtWidgets.QLabel(self.centralwidget)
        self.user_place.setGeometry(QtCore.QRect(40, 500, 51, 51))
        self.user_place.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                      "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                      "")
        self.user_place.setObjectName("user_place")
        self.user_place_name = QtWidgets.QLabel(self.centralwidget)
        self.user_place_name.setGeometry(QtCore.QRect(110, 500, 541, 51))
        self.user_place_name.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                           "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                           "")
        self.user_place_name.setObjectName("user_place_name")
        self.first_place_score = QtWidgets.QLabel(self.centralwidget)
        self.first_place_score.setGeometry(QtCore.QRect(670, 170, 121, 61))
        self.first_place_score.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                             "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                             "")
        self.first_place_score.setObjectName("first_place_score")
        self.second_place_score = QtWidgets.QLabel(self.centralwidget)
        self.second_place_score.setGeometry(QtCore.QRect(670, 250, 121, 61))
        self.second_place_score.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                              "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                              "")
        self.second_place_score.setObjectName("second_place_score")
        self.third_place_score = QtWidgets.QLabel(self.centralwidget)
        self.third_place_score.setGeometry(QtCore.QRect(670, 330, 121, 51))
        self.third_place_score.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                             "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                             "")
        self.third_place_score.setObjectName("third_place_score")
        self.user_place_score = QtWidgets.QLabel(self.centralwidget)
        self.user_place_score.setGeometry(QtCore.QRect(670, 500, 121, 51))
        self.user_place_score.setStyleSheet(";background-color: rgb(0, 0, 0);\n"
                                            "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                            "")
        self.user_place_score.setObjectName("user_place_score")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(640, 40, 121, 81))
        self.pushButton.setStyleSheet(";background-color: rgb(162, 47, 255);\n"
                                      "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow, user_list, curr_user)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.check_for_button(MainWindow)

    def check_for_button(self, MainWindow):
        self.pushButton.clicked.connect(lambda: self.exitpressed(MainWindow))

    def exitpressed(self, MainWindow):
        print("exit pressed")
        self._mutex.lock()
        self.client.screen_state = 2
        self._mutex.unlock()
        MainWindow.close()

    def retranslateUi(self, MainWindow, user_list, curr_user):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.leaderboard_title.setText(_translate("MainWindow",
                                                  "<html><head/><body><p><span style=\" font-size:26pt; color:#aaaaff;\">top players leaderboard</span></p></body></html>"))
        self.first_place.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:26pt; color:#ffaa00;\">1.</span></p></body></html>"))
        self.second_place.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" color:#ffaa00;\">2.</span></p></body></html>"))
        self.third_place.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" color:#ffaa00;\">3.</span></p></body></html>"))
        self.first_place_name.setText(_translate("MainWindow",
                                                 "<html><head/><body><p><span style=\" font-size:26pt; color:#ffaa00;\">"+user_list[0][0]+"</span></p></body></html>"))
        self.second_place_name.setText(_translate("MainWindow",
                                                  "<html><head/><body><p><span style=\" font-size:26pt; color:#ffaa00;\">"+user_list[1][0]+"</span></p></body></html>"))
        self.third_place_name.setText(_translate("MainWindow",
                                                 "<html><head/><body><p><span style=\" font-size:26pt; color:#ffaa00;\">"+user_list[2][0]+"</span></p></body></html>"))
        self.user_place.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-size:26pt; color:#ff00ff;\">"+curr_user[0]+".</span></p></body></html>"))
        self.user_place_name.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:26pt; color:#ff00ff;\">"+curr_user[1]+"</span></p></body></html>"))
        self.first_place_score.setText(_translate("MainWindow",
                                                  "<html><head/><body><p><span style=\" font-size:26pt; color:#ffaa00;\">"+user_list[0][1]+"</span></p></body></html>"))
        self.second_place_score.setText(_translate("MainWindow",
                                                   "<html><head/><body><p><span style=\" font-size:26pt; color:#ffaa00;\">"+user_list[1][1]+"</span></p></body></html>"))
        self.third_place_score.setText(_translate("MainWindow",
                                                  "<html><head/><body><p><span style=\" font-size:26pt; color:#ffaa00;\">"+user_list[2][1]+"</span></p></body></html>"))
        self.user_place_score.setText(_translate("MainWindow",
                                                 "<html><head/><body><p><span style=\" font-size:26pt; color:#ff00ff;\">"+curr_user[2]+"</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "exit"))


def show_leaderboard_window(window, user_list, curr_user):
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    window.setupUi(MainWindow, user_list, curr_user)
    MainWindow.show()
    sys.exit(app.exec_())