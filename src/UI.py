# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnCompileCode = QtWidgets.QPushButton(self.centralwidget)
        self.btnCompileCode.setGeometry(QtCore.QRect(10, 20, 94, 36))
        self.btnCompileCode.setObjectName("btnCompileCode")
        self.btnRunCode = QtWidgets.QPushButton(self.centralwidget)
        self.btnRunCode.setGeometry(QtCore.QRect(110, 20, 94, 36))
        self.btnRunCode.setObjectName("btnRunCode")
        self.codeEditor = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.codeEditor.setGeometry(QtCore.QRect(10, 60, 581, 441))
        self.codeEditor.setPlainText("")
        self.codeEditor.setObjectName("codeEditor")
        self.btnSaveCode = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveCode.setGeometry(QtCore.QRect(210, 20, 94, 36))
        self.btnSaveCode.setObjectName("btnSaveCode")
        self.btnOpenCode = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenCode.setGeometry(QtCore.QRect(310, 20, 94, 36))
        self.btnOpenCode.setObjectName("btnOpenCode")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NASMedit"))
        self.btnCompileCode.setText(_translate("MainWindow", "Compile"))
        self.btnRunCode.setText(_translate("MainWindow", "Run"))
        self.btnSaveCode.setText(_translate("MainWindow", "Save"))
        self.btnOpenCode.setText(_translate("MainWindow", "Open"))
