import sys, os, cv2
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import numpy as np
from slantAnalyser import SlantAnalyser
from zonesAnalyzer import ZonesAnalyzer
from tDataExtractor import Colors, TDataExtractor
from dist_analyzer import DistAnalyzer
from tAnalyzer import TAnalyzer
import mainWindow_ui, slantWindow_ui, zoneWindow_ui, tChecker_ui, distWindow_ui, tkFileDialog
import Tkinter as tk
import json



graphology = None


class MainWindow(QMainWindow, mainWindow_ui.Ui_Graphology):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.btnLoadImage.clicked.connect(self.loadImageMethod)
        self.buttonSlant.clicked.connect(self.openSlantChecker)
        self.buttonZone.clicked.connect(self.openZoneChecker)
        self.buttonT.clicked.connect(self.openTAnalyzer)
        self.buttonDist.clicked.connect(self.openDistChecker)
        self.slantChecker = SlantWindow()
        self.zoneChecker = ZoneWindow()
        self.tAnalyzer = TWindow()
        self.distChecker = DistWindow()


    def loadImageMethod(self):
        root = tk.Tk()
        root.withdraw()
        picture_file_path = tkFileDialog.askopenfilename(filetypes=(("Pictures", "*.png"), ("Pictures", "*.jpg"), ("All files", "*.*") ))
        pixmap = QtGui.QPixmap(picture_file_path)
        pixmap_resized = pixmap.scaled(self.mainPicture.size(), QtCore.Qt.KeepAspectRatio,
                                       QtCore.Qt.SmoothTransformation)
        self.mainPicture.setPixmap(pixmap_resized)

    def openSlantChecker(self):
        pixmap = self.mainPicture.pixMapToShare
        pixmap_resized = pixmap.scaled(self.slantChecker.mainPicture.size(), QtCore.Qt.KeepAspectRatio,
                                       QtCore.Qt.SmoothTransformation)
        pixmap_resized.save("samples/sample1.png", "PNG")
        self.slantChecker.mainPicture.setPixmap(pixmap_resized)
        self.slantChecker.show()

    def openZoneChecker(self):
        counter = 0
        pixmap = self.mainPicture.pixMapToShare
        pixmap_resized = pixmap.scaled(self.zoneChecker.mainPicture.size(), QtCore.Qt.KeepAspectRatio,
                                       QtCore.Qt.SmoothTransformation)
        pixmap_resized.save("samples/sample1.png", "PNG")
        self.zoneChecker.mainPicture.setPixmap(pixmap_resized)
        self.zoneChecker.zoneCheckerChangeSliders()
        self.zoneChecker.show()

    def openTAnalyzer(self):
        pixmap = self.mainPicture.pixMapToShare
        pixmap_resized = pixmap.scaled(self.tAnalyzer.mainPicture.size(), QtCore.Qt.KeepAspectRatio,
                                       QtCore.Qt.SmoothTransformation)
        pixmap_resized.save("samples/sample1.png", "PNG")
        self.tAnalyzer.mainPicture.setPixmap(pixmap_resized)
        self.tAnalyzer.show()

    def openDistChecker(self):
        pixmap = self.mainPicture.pixMapToShare
        pixmap_resized = pixmap.scaled(self.distChecker.mainPicture.size(), QtCore.Qt.KeepAspectRatio,
                                       QtCore.Qt.SmoothTransformation)
        pixmap_resized.save("samples/sample1.png", "PNG")
        self.distChecker.mainPicture.setPixmap(pixmap_resized)
        self.distChecker.distCheckerChangeSliders()
        self.distChecker.show()


class SlantWindow(QMainWindow, slantWindow_ui.Ui_Slantchecker):

    def __init__(self, parent=None):
        super(SlantWindow,self).__init__(parent)
        self.setupUi(self)
        self.angleSlider.valueChanged.connect(self.onChange)
        self.distanceSlider.valueChanged.connect(self.onChange)

    def onChange(self):
        self.angleCount.setNum(self.angleSlider.value())
        self.distanceCount.setNum(self.distanceSlider.value())

        img = cv2.imread("samples/sample1.png", -1)
        linesGap =  self.distanceSlider.value()
        angle = self.angleSlider.value()

        a = np.tan(angle * 2 * np.pi / 360)

        width, height = img.shape[:2]

        for i in np.arange(-5 * width, 5 * width, int(linesGap)):
            x1 = i
            y1 = 0
            x2 = int((height + a * x1) / a)
            y2 = height
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        analysis = SlantAnalyser.analyzeSlant([180 - angle])

        self.analysis.setText(analysis[0]["slantType"] + '\n' + analysis[0]["analysis"])

        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        qPixToCover = QtGui.QPixmap.fromImage(qImg)
        self.mainPicture.setPixmap(qPixToCover)


class ZoneWindow(QMainWindow, zoneWindow_ui.Ui_Zonechecker):

    def __init__(self, parent=None):
        super(ZoneWindow,self).__init__(parent)
        self.setupUi(self)
        self.uztSlider.valueChanged.connect(self.onChange)
        self.mztSlider.valueChanged.connect(self.onChange)
        self.bztSlider.valueChanged.connect(self.onChange)
        self.bzbSlider.valueChanged.connect(self.onChange)


    def zoneCheckerChangeSliders(self):
        img = cv2.imread("samples/sample1.png", -1)
        height, width = img.shape[:2]
        self.uztSlider.setRange(0, height)
        self.mztSlider.setRange(0, height)
        self.bztSlider.setRange(0, height)
        self.bzbSlider.setRange(0, height)


    def onChange(self):
        self.uztCount.setNum(self.uztSlider.value())
        self.mztCount.setNum(self.mztSlider.value())
        self.bztCount.setNum(self.bztSlider.value())
        self.bzbCount.setNum(self.bzbSlider.value())

        img = cv2.imread("samples/sample1.png", -1)

        upperZoneTop = self.uztSlider.value()
        middleZoneTop = self.mztSlider.value()
        bottomZoneTop = self.bztSlider.value()
        bottomZoneBottom = self.bzbSlider.value()

        cv2.line(img, (0, upperZoneTop), (20000, upperZoneTop), (0, 255, 0), 2);
        cv2.line(img, (0, middleZoneTop), (20000, upperZoneTop), (0, 255, 0), 2)
        cv2.line(img, (0, bottomZoneTop), (20000, upperZoneTop), (0, 255, 0), 2)
        cv2.line(img, (0, bottomZoneBottom), (20000, upperZoneTop), (0, 255, 0), 2)

        separators = [upperZoneTop, middleZoneTop, bottomZoneTop, bottomZoneBottom]
        text = ZonesAnalyzer.analyze(separators)
        json_string = json.dumps(text)
        self.analysis.setText(json_string)


        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        qPixToCover = QtGui.QPixmap.fromImage(qImg)
        self.mainPicture.setPixmap(qPixToCover)


class DistWindow(QMainWindow, distWindow_ui.Ui_Distchecker):

    def __init__(self, parent=None):
        super(DistWindow,self).__init__(parent)
        self.setupUi(self)
        self.bottomSlider.valueChanged.connect(self.onChange)
        self.topSlider.valueChanged.connect(self.onChange)
        # self.mainPicture.mousePressEvent(self, self.getClickPosition)


    def onChange(self):
        self.bottomCount.setNum(self.bottomSlider.value())
        self.topCount.setNum(self.topSlider.value())

        img = cv2.imread("samples/sample1.png", -1)

        top =  self.topSlider.value()
        bottom = self.bottomSlider.value()

        cv2.line(img, (0, bottom), (20000, bottom), (255, 0, 0), 1)
        cv2.line(img, (0, top), (20000, bottom), (255, 0, 0), 1)

        self.text = bottom - top

        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        qPixToCover = QtGui.QPixmap.fromImage(qImg)
        self.mainPicture.setPixmap(qPixToCover)

    def distCheckerChangeSliders(self):
        img = cv2.imread("samples/sample1.png", -1)
        height, width = img.shape[:2]
        self.bottomSlider.setRange(0, height)
        self.topSlider.setRange(0, height)

    def getClickPosition(self,event):
        print event.pos()


class TWindow(QMainWindow, tChecker_ui.Ui_Tanalyzer):

    def __init__(self, parent=None):
        super(TWindow,self).__init__(parent)
        self.setupUi(self)
        self.analyzeButton.clicked.connect(self.tAnalyzing)

    def tAnalyzing(self):
        img = cv2.imread("samples/sample1.png", -1)

        extractor = TDataExtractor(img)
        extractor.analyze()

        data = extractor.getData()
        resultImg = extractor.getResultImg()

        print 'got data:'
        print data

        print 'analysis:'
        print TAnalyzer.analyze(data)

        json_string = json.dumps(TAnalyzer.analyze(data))
        self.analysis.setText(json_string)

        height, width, channel = resultImg.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(resultImg.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        qPixToCover = QtGui.QPixmap.fromImage(qImg)
        self.mainPicture.setPixmap(qPixToCover)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    graphology = MainWindow()
    graphology.show()
    sys.exit(app.exec_())