# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets, QtGui
from label import RubberbandEnhancedLabel
from slant_check_window2 import Ui_Slantchecker
import Tkinter as tk
import tkFileDialog

class Ui_Graphology(object):
    def setupUi(self, Graphology):
        Graphology.setObjectName("Graphology")
        Graphology.resize(1081, 632)
        self.mainContainer = QtWidgets.QWidget(Graphology)
        self.mainContainer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainContainer.setObjectName("mainContainer")
        self.gridLayout = QtWidgets.QGridLayout(self.mainContainer)
        self.gridLayout.setContentsMargins(12, 12, 12, 12)
        self.gridLayout.setHorizontalSpacing(40)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.btnLoadImage = QtWidgets.QPushButton(self.mainContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLoadImage.sizePolicy().hasHeightForWidth())
        self.btnLoadImage.setSizePolicy(sizePolicy)
        self.btnLoadImage.setFlat(False)
        self.btnLoadImage.setObjectName("btnLoadImage")
        self.gridLayout.addWidget(self.btnLoadImage, 0, 0, 1, 1)
        self.btnLoadImage.clicked.connect(self.loadImageMethod)
        self.analysis = QtWidgets.QPushButton(self.mainContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analysis.sizePolicy().hasHeightForWidth())
        self.analysis.setSizePolicy(sizePolicy)
        self.analysis.setFlat(False)
        self.analysis.setObjectName("analysis")
        self.gridLayout.addWidget(self.analysis, 0, 1, 1, 1)
        self.analysis.clicked.connect(self.grabPartOfPicture)
        self.featureBox = QtWidgets.QGroupBox(self.mainContainer)
        self.featureBox.setObjectName("featureBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.featureBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonSlant = QtWidgets.QPushButton(self.featureBox)
        self.buttonSlant.setObjectName("buttonSlant")
        self.verticalLayout.addWidget(self.buttonSlant)
        self.pushButton_5 = QtWidgets.QPushButton(self.featureBox)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.featureBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.featureBox)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.gridLayout.addWidget(self.featureBox, 1, 5, 2, 1)
        self.mainPicture = RubberbandEnhancedLabel(self.mainContainer)
        self.mainPicture.setAutoFillBackground(True)
        self.mainPicture.setFrameShape(QtWidgets.QFrame.Box)
        self.mainPicture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPicture.setLineWidth(3)
        self.mainPicture.setObjectName("mainPicture")
        self.mainPicture.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.mainPicture, 1, 0, 2, 4)
        self.scrollArea = QtWidgets.QScrollArea(self.mainContainer)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(225, 600))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 223, 539))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_4.setMaximumSize(QtCore.QSize(225, 400))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout.addWidget(self.scrollArea, 1, 6, 1, 1)
        Graphology.setCentralWidget(self.mainContainer)
        self.statusBar = QtWidgets.QStatusBar(Graphology)
        self.statusBar.setObjectName("statusBar")
        Graphology.setStatusBar(self.statusBar)
        self.retranslateUi(Graphology)
        QtCore.QMetaObject.connectSlotsByName(Graphology)

    def retranslateUi(self, Graphology):
        _translate = QtCore.QCoreApplication.translate
        Graphology.setWindowTitle(_translate("Graphology", "Graphology"))
        self.btnLoadImage.setText(_translate("Graphology", "Load Image"))
        self.analysis.setText(_translate("Graphology", "Analysis"))
        self.featureBox.setTitle(_translate("Graphology", "Features"))
        self.buttonSlant.setText(_translate("Graphology", "Slant Checker"))
        self.pushButton_5.setText(_translate("Graphology", "PushButton"))
        self.pushButton_4.setText(_translate("Graphology", "PushButton"))
        self.pushButton_6.setText(_translate("Graphology", "PushButton"))
        self.mainPicture.setText(_translate("Graphology", ""))
        self.label_2.setText(_translate("Graphology", "TextLabel"))
        self.label_3.setText(_translate("Graphology", "TextLabel"))
        self.label_4.setText(_translate("Graphology", "TextLabel"))

    def loadImageMethod(self):
        root = tk.Tk()
        root.withdraw()
        picture_file_path = tkFileDialog.askopenfilename(filetypes=(("Pictures", "*.jpg"), ("All files", "*.*") ))
        pixmap = QtGui.QPixmap(picture_file_path)
        pixmap_resized = pixmap.scaled(self.mainPicture.size(), QtCore.Qt.KeepAspectRatio)
        self.mainPicture.setPixmap(pixmap_resized)

    def grabPartOfPicture(self):
        self.pixmap = self.mainPicture.pixMapToShare

