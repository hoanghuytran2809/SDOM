from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        # Set the background color of the main window to white
        MainWindow.setStyleSheet("background-color: white;")
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 700, 30))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        
        # Set the text color of the label to black
        self.label.setStyleSheet("color: black;")
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Mouse events will be displayed here"))

class MainWindowApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def mousePressEvent(self, event):
        button = event.button()
        if button == QtCore.Qt.MouseButton.LeftButton:
            self.label.setText('Left Button Pressed')
        elif button == QtCore.Qt.MouseButton.RightButton:
            self.label.setText('Right Button Pressed')
        elif button == QtCore.Qt.MouseButton.MiddleButton:
            self.label.setText('Middle Button Pressed')

    def mouseReleaseEvent(self, event):
        button = event.button()
        if button == QtCore.Qt.MouseButton.LeftButton:
            self.label.setText('Left Button Released')
        elif button == QtCore.Qt.MouseButton.RightButton:
            self.label.setText('Right Button Released')
        elif button == QtCore.Qt.MouseButton.MiddleButton:
            self.label.setText('Middle Button Released')

    def mouseMoveEvent(self, event):
        self.label.setText(f'Mouse Move: ({event.x()}, {event.y()})')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindowApp()
    MainWindow.show()
    sys.exit(app.exec())
