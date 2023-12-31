# -*- coding: utf-8 -*-
import os
from datetime import datetime

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from process import Process


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 800, 590))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setAutoRepeatInterval(100)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 21))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Générateur de bdd photos au format JSON"))
        self.pushButton.setText(_translate("MainWindow", "Lancer la création du fichier JSON"))
        self.pushButton.setGeometry(10, 0, 300, 300)


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialisation de l'interface graphique
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connectez des signaux et des slots
        self.ui.pushButton.clicked.connect(self.button_clicked)


        self.textEdit = QTextEdit(self.ui.centralwidget)
        self.textEdit.setGeometry(
            QtCore.QRect(10, 200, 700, 300))  # Définir la position et la taille de la fenêtre de texte
        self.ui.verticalLayout.addWidget(self.textEdit)

    def button_clicked(self):
        process = Process()
        process.exifImageJason()
        self.textEdit.append("##### Fichiers traités ##### :\n")
        liste = process.listTraitee
        for i in range(len(liste)):
            self.textEdit.append(liste[i])

        self.textEdit.append("\n##### Fichiers en erreur ##### :\n")
        listeE = process.listErreur
        for i in range(len(listeE)):
            self.textEdit.append(listeE[i])
