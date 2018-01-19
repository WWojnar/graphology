# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tChecker.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tanalyzer(object):
    def setupUi(self, Tanalyzer):
        Tanalyzer.setObjectName("Tanalyzer")
        Tanalyzer.resize(525, 653)
        Tanalyzer.setMaximumSize(QtCore.QSize(16777215, 16777210))
        Tanalyzer.setSizeIncrement(QtCore.QSize(1, 0))
        Tanalyzer.setAutoFillBackground(False)
        self.mainContainer = QtWidgets.QWidget(Tanalyzer)
        self.mainContainer.setObjectName("mainContainer")
        self.gridLayout = QtWidgets.QGridLayout(self.mainContainer)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.mainContainer)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.analyzeButton = QtWidgets.QPushButton(self.groupBox)
        self.analyzeButton.setObjectName("analyzeButton")
        self.verticalLayout.addWidget(self.analyzeButton)
        self.saveButton = QtWidgets.QPushButton(self.groupBox)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)
        self.analysis = QtWidgets.QLabel(self.mainContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analysis.sizePolicy().hasHeightForWidth())
        self.analysis.setSizePolicy(sizePolicy)
        self.analysis.setFrameShape(QtWidgets.QFrame.Box)
        self.analysis.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analysis.setLineWidth(3)
        self.analysis.setText("")
        self.analysis.setWordWrap(True)
        self.analysis.setObjectName("analysis")
        self.gridLayout.addWidget(self.analysis, 2, 1, 1, 1)
        self.mainPicture = QtWidgets.QLabel(self.mainContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPicture.sizePolicy().hasHeightForWidth())
        self.mainPicture.setSizePolicy(sizePolicy)
        self.mainPicture.setFrameShape(QtWidgets.QFrame.Box)
        self.mainPicture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPicture.setLineWidth(3)
        self.mainPicture.setText("")
        self.mainPicture.setPixmap(QtGui.QPixmap("graphology/white.bmp"))
        self.mainPicture.setScaledContents(False)
        self.mainPicture.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mainPicture.setObjectName("mainPicture")
        self.gridLayout.addWidget(self.mainPicture, 0, 0, 2, 2)
        Tanalyzer.setCentralWidget(self.mainContainer)

        self.retranslateUi(Tanalyzer)
        QtCore.QMetaObject.connectSlotsByName(Tanalyzer)

    def retranslateUi(self, Tanalyzer):
        _translate = QtCore.QCoreApplication.translate
        Tanalyzer.setWindowTitle(_translate("Tanalyzer", "T Analyzer"))
        self.groupBox.setTitle(_translate("Tanalyzer", "Operations"))
        self.analyzeButton.setText(_translate("Tanalyzer", "Analyze"))
        self.saveButton.setText(_translate("Tanalyzer", "Save"))

