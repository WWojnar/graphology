# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slantChecker.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Slantchecker(object):
    def setupUi(self, Slantchecker):
        Slantchecker.setObjectName("Slantchecker")
        Slantchecker.resize(939, 758)
        Slantchecker.setMaximumSize(QtCore.QSize(16777215, 16777210))
        Slantchecker.setSizeIncrement(QtCore.QSize(1, 0))
        Slantchecker.setAutoFillBackground(False)
        self.mainContainer = QtWidgets.QWidget(Slantchecker)
        self.mainContainer.setObjectName("mainContainer")
        self.gridLayout = QtWidgets.QGridLayout(self.mainContainer)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.mainContainer)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.distanceSlider = QtWidgets.QSlider(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distanceSlider.sizePolicy().hasHeightForWidth())
        self.distanceSlider.setSizePolicy(sizePolicy)
        self.distanceSlider.setMinimum(1)
        self.distanceSlider.setMaximum(200)
        self.distanceSlider.setPageStep(1)
        self.distanceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.distanceSlider.setInvertedAppearance(False)
        self.distanceSlider.setSliderPosition(50)
        self.distanceSlider.setInvertedControls(False)
        self.distanceSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.distanceSlider.setObjectName("horizontalSlider")
        self.verticalLayout_3.addWidget(self.distanceSlider)
        self.distanceCount = QtWidgets.QLabel(self.groupBox_2)
        self.distanceCount.setSizeIncrement(QtCore.QSize(3, 0))
        self.distanceCount.setObjectName("distanceCount")
        self.verticalLayout_3.addWidget(self.distanceCount)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.angleSlider = QtWidgets.QSlider(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angleSlider.sizePolicy().hasHeightForWidth())
        self.angleSlider.setSizePolicy(sizePolicy)
        self.angleSlider.setMinimum(0)
        self.angleSlider.setMaximum(180)
        self.angleSlider.setPageStep(1)
        self.angleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.angleSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.angleSlider.setSliderPosition(90)
        self.angleSlider.setObjectName("horizontalSlider_2")
        self.verticalLayout_2.addWidget(self.angleSlider)
        self.angleCount = QtWidgets.QLabel(self.groupBox_3)
        self.angleCount.setTextFormat(QtCore.Qt.AutoText)
        self.angleCount.setObjectName("angleCount")
        self.verticalLayout_2.addWidget(self.angleCount)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.saveButton = QtWidgets.QPushButton(self.groupBox)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 3)
        self.analysis = QtWidgets.QLabel(self.mainContainer)
        self.analysis.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.analysis.setObjectName("analysis")
        self.gridLayout.addWidget(self.analysis, 0, 2, 2, 1)
        self.mainPicture = QtWidgets.QLabel(self.mainContainer)
        self.mainPicture.setAutoFillBackground(True)
        self.mainPicture.setFrameShape(QtWidgets.QFrame.Box)
        self.mainPicture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPicture.setLineWidth(3)
        self.mainPicture.setAlignment(QtCore.Qt.AlignCenter)
        self.mainPicture.setObjectName("mainPicture")
        self.gridLayout.addWidget(self.mainPicture, 0, 0, 2, 2)
        Slantchecker.setCentralWidget(self.mainContainer)
        self.retranslateUi(Slantchecker)
        QtCore.QMetaObject.connectSlotsByName(Slantchecker)

    def retranslateUi(self, Slantchecker):
        _translate = QtCore.QCoreApplication.translate
        Slantchecker.setWindowTitle(_translate("Slantchecker", "Slant Checker"))
        self.groupBox.setTitle(_translate("Slantchecker", "Operations"))
        self.groupBox_2.setTitle(_translate("Slantchecker", "Distance"))
        self.distanceCount.setText(_translate("Slantchecker", "50"))
        self.groupBox_3.setTitle(_translate("Slantchecker", "Angle"))
        self.angleCount.setText(_translate("Slantchecker", "90"))
        self.saveButton.setText(_translate("Slantchecker", "Save"))
        self.analysis.setText(_translate("Slantchecker", "Analysis"))

