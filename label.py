from PyQt5 import QtGui, QtCore, QtWidgets

class RubberbandEnhancedLabel(QtWidgets.QLabel):

    cropQPixmap = 0
    def __init__(self, parent=None):
        QtWidgets.QLabel.__init__(self, parent)
        self.selection = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, self)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            position = QtCore.QPoint(event.pos())
            if self.selection.isVisible():
                # visible selection
                if (self.upper_left - position).manhattanLength() < 20:
                    # close to upper left corner, drag it
                    self.mode = "drag_upper_left"
                elif (self.lower_right - position).manhattanLength() < 20:
                    # close to lower right corner, drag it
                    self.mode = "drag_lower_right"
                else:
                    # clicked somewhere else, hide selection
                    self.pixMapToShare = self.cropQPixmap
                    self.pixMapToShare.save("samples/sample2.png","PNG")
                    self.selection.hide()
            else:
                # no visible selection, start new selection
                self.upper_left = position
                self.lower_right = position
                self.mode = "drag_lower_right"
                self.selection.show()

    def mouseMoveEvent(self, event):
        if self.selection.isVisible():
            # visible selection
            if self.mode is "drag_lower_right":
                self.lower_right = QtCore.QPoint(event.pos())
            elif self.mode is "drag_upper_left":
                self.upper_left = QtCore.QPoint(event.pos())
            # update geometry
            self.selection.setGeometry(QtCore.QRect(self.upper_left, self.lower_right).normalized())
            currentQRect = self.selection.geometry()
            self.cropQPixmap = self.pixmap().copy(currentQRect)


