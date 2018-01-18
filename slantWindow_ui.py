# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slantChecker.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Slantchecker(object):
    def setupUi(self, Slantchecker):
        Slantchecker.setObjectName("slantChecker")
        Slantchecker.resize(894, 507)
        Slantchecker.setAutoFillBackground(False)
        self.mainContainer = QtWidgets.QWidget(Slantchecker)
        self.mainContainer.setObjectName("mainContainer")
        self.gridLayout = QtWidgets.QGridLayout(self.mainContainer)
        self.gridLayout.setObjectName("gridLayout")
        self.analysis = QtWidgets.QLabel(self.mainContainer)
        self.analysis.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.analysis.setObjectName("analysis")
        self.gridLayout.addWidget(self.analysis, 1, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.mainContainer)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.clearButton = QtWidgets.QPushButton(self.groupBox)
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout.addWidget(self.clearButton)
        self.saveButton = QtWidgets.QPushButton(self.groupBox)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)
        self.spareButton = QtWidgets.QPushButton(self.groupBox)
        self.spareButton.setObjectName("spareButton")
        self.verticalLayout.addWidget(self.spareButton)
        self.gridLayout.addWidget(self.groupBox, 2, 2, 1, 1)
        self.mainPicture = QtWidgets.QLabel(self.mainContainer)
        self.mainPicture.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.mainPicture.setText("")
        self.mainPicture.setObjectName("mainPicture")
        self.mainPicture.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.mainPicture, 1, 1, 2, 1)
        Slantchecker.setCentralWidget(self.mainContainer)

        self.retranslateUi(Slantchecker)
        QtCore.QMetaObject.connectSlotsByName(Slantchecker)

    def retranslateUi(self, slantChecker):
        _translate = QtCore.QCoreApplication.translate
        slantChecker.setWindowTitle(_translate("slantChecker", "Slant Checker"))
        self.analysis.setText(_translate("slantChecker", "Analysis"))
        self.groupBox.setTitle(_translate("slantChecker", "Operations"))
        self.clearButton.setText(_translate("slantChecker", "Clear"))
        self.saveButton.setText(_translate("slantChecker", "Save"))
        self.spareButton.setText(_translate("slantChecker", "Optional"))

