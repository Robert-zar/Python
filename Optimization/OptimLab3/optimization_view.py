# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optimization.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Widget")
        MainWindow.resize(841, 600)
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.lab_1 = QtWidgets.QWidget()
        self.lab_1.setObjectName("lab_1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.lab_1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.lab_1)
        self.groupBox.setObjectName("groupBox")
        self.textEdit_lab_1 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_lab_1.setGeometry(QtCore.QRect(270, 60, 491, 441))
        self.textEdit_lab_1.setObjectName("textEdit_lab_1")
        self.pushButton_lab_1 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_lab_1.setGeometry(QtCore.QRect(20, 440, 241, 61))
        self.pushButton_lab_1.setObjectName("pushButton_lab_1")
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.tabWidget.addTab(self.lab_1, "")
        self.lab_2 = QtWidgets.QWidget()
        self.lab_2.setObjectName("lab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.lab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.lab_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit_lab_2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_lab_2.setGeometry(QtCore.QRect(270, 60, 491, 441))
        self.textEdit_lab_2.setObjectName("textEdit_lab_2")
        self.pushButton_lab_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_lab_2.setGeometry(QtCore.QRect(20, 440, 241, 61))
        self.pushButton_lab_2.setObjectName("pushButton_lab_2")
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.lab_2, "")
        self.lab_3 = QtWidgets.QWidget()
        self.lab_3.setObjectName("lab_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.lab_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.lab_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit_lab_3 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_lab_3.setGeometry(QtCore.QRect(270, 60, 491, 441))
        self.textEdit_lab_3.setObjectName("textEdit_lab_3")
        self.pushButton_lab_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_lab_3.setGeometry(QtCore.QRect(20, 440, 241, 61))
        self.pushButton_lab_3.setObjectName("pushButton_lab_3")
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.lab_3, "")
        self.lab_4 = QtWidgets.QWidget()
        self.lab_4.setObjectName("lab_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.lab_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.lab_4)
        self.groupBox_4.setObjectName("groupBox_4")
        self.textEdit_lab_4 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_lab_4.setGeometry(QtCore.QRect(270, 60, 491, 441))
        self.textEdit_lab_4.setObjectName("textEdit_lab_4")
        self.pushButton_lab_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_lab_4.setGeometry(QtCore.QRect(20, 440, 241, 61))
        self.pushButton_lab_4.setObjectName("pushButton_lab_4")
        self.horizontalLayout_5.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.lab_4, "")
        self.lab_5 = QtWidgets.QWidget()
        self.lab_5.setObjectName("lab_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.lab_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.lab_5)
        self.groupBox_5.setObjectName("groupBox_5")
        self.textEdit_lab_5 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_lab_5.setGeometry(QtCore.QRect(270, 60, 491, 441))
        self.textEdit_lab_5.setObjectName("textEdit_lab_5")
        self.pushButton_lab_5 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_lab_5.setGeometry(QtCore.QRect(20, 440, 241, 61))
        self.pushButton_lab_5.setObjectName("pushButton_lab_5")
        self.horizontalLayout_6.addWidget(self.groupBox_5)
        self.tabWidget.addTab(self.lab_5, "")
        self.lab_6 = QtWidgets.QWidget()
        self.lab_6.setObjectName("lab_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.lab_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_6 = QtWidgets.QGroupBox(self.lab_6)
        self.groupBox_6.setObjectName("groupBox_6")
        self.textEdit_lab_6 = QtWidgets.QTextEdit(self.groupBox_6)
        self.textEdit_lab_6.setGeometry(QtCore.QRect(270, 60, 491, 441))
        self.textEdit_lab_6.setObjectName("textEdit_lab_6")
        self.pushButton_lab_6 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_lab_6.setGeometry(QtCore.QRect(20, 440, 241, 61))
        self.pushButton_lab_6.setObjectName("pushButton_lab_6")
        self.horizontalLayout_7.addWidget(self.groupBox_6)
        self.tabWidget.addTab(self.lab_6, "")
        self.lab_7 = QtWidgets.QWidget()
        self.lab_7.setObjectName("lab_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.lab_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox_7 = QtWidgets.QGroupBox(self.lab_7)
        self.groupBox_7.setObjectName("groupBox_7")
        self.textEdit_lab_7 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_lab_7.setGeometry(QtCore.QRect(270, 60, 491, 441))
        self.textEdit_lab_7.setObjectName("textEdit_lab_7")
        self.pushButton_lab_7 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_lab_7.setGeometry(QtCore.QRect(20, 440, 241, 61))
        self.pushButton_lab_7.setObjectName("pushButton_lab_7")
        self.horizontalLayout_8.addWidget(self.groupBox_7)
        self.tabWidget.addTab(self.lab_7, "")
        self.lab_8 = QtWidgets.QWidget()
        self.lab_8.setObjectName("lab_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.lab_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.groupBox_8 = QtWidgets.QGroupBox(self.lab_8)
        self.groupBox_8.setObjectName("groupBox_8")
        self.textEdit_lab_8 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_lab_8.setGeometry(QtCore.QRect(270, 60, 491, 441))
        self.textEdit_lab_8.setObjectName("textEdit_lab_8")
        self.pushButton_lab_8 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_lab_8.setGeometry(QtCore.QRect(20, 440, 241, 61))
        self.pushButton_lab_8.setObjectName("pushButton_lab_8")
        self.horizontalLayout_9.addWidget(self.groupBox_8)
        self.tabWidget.addTab(self.lab_8, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Widget", "Widget"))
        self.groupBox.setTitle(_translate("Widget", "    ???????????????????????? ??????????"))
        self.pushButton_lab_1.setText(_translate("Widget", "??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lab_1), _translate("Widget", "laba 1"))
        self.groupBox_2.setTitle(_translate("Widget", "    ????????????????"))
        self.pushButton_lab_2.setText(_translate("Widget", "??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lab_2), _translate("Widget", "laba 2"))
        self.groupBox_3.setTitle(_translate("Widget", "???????????????????????? ????????????????"))
        self.pushButton_lab_3.setText(_translate("Widget", "??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lab_3), _translate("Widget", "laba 3"))
        self.groupBox_4.setTitle(_translate("Widget", "???????????????? ?????? ????????????"))
        self.pushButton_lab_4.setText(_translate("Widget", "??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lab_4), _translate("Widget", "laba 4"))
        self.groupBox_5.setTitle(_translate("Widget", "???????????????? ????????????????"))
        self.pushButton_lab_5.setText(_translate("Widget", "??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lab_5), _translate("Widget", "laba 5"))
        self.groupBox_6.setTitle(_translate("Widget", "???????????????? ????????????????"))
        self.pushButton_lab_6.setText(_translate("Widget", "??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lab_6), _translate("Widget", "laba 6"))
        self.groupBox_7.setTitle(_translate("Widget", "?????????????????????????? ????????????????"))
        self.pushButton_lab_7.setText(_translate("Widget", "??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lab_7), _translate("Widget", "laba 7"))
        self.groupBox_8.setTitle(_translate("Widget", "?????????????????? ????????????????"))
        self.pushButton_lab_8.setText(_translate("Widget", "??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lab_8), _translate("Widget", "laba 8"))
