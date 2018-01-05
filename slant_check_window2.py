
from PyQt5 import QtWidgets
import sys

from PyQt5 import QtCore, QtWidgets


class Ui_Slantchecker(object):


    def setupUi(self, Slantchecker):
        Slantchecker.setObjectName("Graphology")
        Slantchecker.resize(600, 800)
        self.mainContainer = QtWidgets.QWidget(Slantchecker)
        self.mainContainer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainContainer.setObjectName("mainContainer")
        self.gridLayout = QtWidgets.QGridLayout(self.mainContainer)
        self.gridLayout.setContentsMargins(12, 12, 12, 12)
        self.gridLayout.setHorizontalSpacing(40)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.mainPicture = QtWidgets.QLabel(self.mainContainer)
        self.mainPicture.setAutoFillBackground(True)
        self.mainPicture.setFrameShape(QtWidgets.QFrame.Box)
        self.mainPicture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPicture.setLineWidth(3)
        self.mainPicture.setObjectName("mainPicture")
        self.mainPicture.setAlignment(QtCore.Qt.AlignCenter)
        self.sliderDistance = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.gridLayout.addWidget(self.sliderDistance)
        self.sliderAngle = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.gridLayout.addWidget(self.sliderAngle)
        Slantchecker.setCentralWidget(self.mainContainer)
        self.statusBar = QtWidgets.QStatusBar(Slantchecker)
        self.statusBar.setObjectName("statusBar")
        Slantchecker.setStatusBar(self.statusBar)
        QtCore.QMetaObject.connectSlotsByName(Slantchecker)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    slantchecker = QtWidgets.QMainWindow()
    ui = Ui_Slantchecker()
    ui.setupUi(slantchecker)
    slantchecker.show()
    sys.exit(app.exec_())
