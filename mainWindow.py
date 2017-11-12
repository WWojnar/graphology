import sys
from PyQt5 import QtWidgets
from mainWindow_ui import Ui_Graphology

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    graphology = QtWidgets.QMainWindow()
    ui = Ui_Graphology()
    ui.setupUi(graphology)
    graphology.show()
    sys.exit(app.exec_())