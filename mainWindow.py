import sys, os
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import mainWindow_ui
import slantWindow_ui

graphology = None


class MainWindow(QMainWindow, mainWindow_ui.Ui_Graphology):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.buttonSlant.clicked.connect(self.openSlantChecker)
        self.slantChecker = SlantWindow()

    def openSlantChecker(self):

        pixmap = self.mainPicture.pixMapToShare
        print self.slantChecker.mainPicture.size()
        pixmap_resized = pixmap.scaled(self.slantChecker.mainPicture.size(), QtCore.Qt.KeepAspectRatio)
        self.slantChecker.mainPicture.setPixmap(pixmap_resized)
        self.slantChecker.show()


class SlantWindow(QMainWindow, slantWindow_ui.Ui_Slantchecker):

    def __init__(self, parent=None):
        super(SlantWindow,self).__init__(parent)
        self.setupUi(self)

        self.mainPicture.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            print "The sender is:", source.text(), event.pos()
        return super(SlantWindow, self).eventFilter(source, event)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    graphology = MainWindow()
    graphology.show()
    sys.exit(app.exec_())