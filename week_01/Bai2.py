from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 10, 661, 21))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 40, 56, 17))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 40, 56, 17))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 40, 56, 17))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 40, 56, 17))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 70, 56, 17))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 70, 56, 17))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(190, 70, 56, 17))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(260, 70, 56, 17))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(50, 100, 56, 17))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(120, 100, 56, 17))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(190, 100, 56, 17))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(260, 100, 56, 17))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(340, 40, 56, 17))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(340, 70, 56, 17))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(340, 100, 56, 17))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(340, 130, 56, 17))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_clear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(340, 160, 56, 17))
        self.pushButton_clear.setObjectName("pushButton_clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to functions
        self.pushButton.clicked.connect(lambda: self.button_pressed("1"))
        self.pushButton_2.clicked.connect(lambda: self.button_pressed("2"))
        self.pushButton_3.clicked.connect(lambda: self.button_pressed("3"))
        self.pushButton_4.clicked.connect(lambda: self.button_pressed("4"))
        self.pushButton_5.clicked.connect(lambda: self.button_pressed("5"))
        self.pushButton_6.clicked.connect(lambda: self.button_pressed("6"))
        self.pushButton_7.clicked.connect(lambda: self.button_pressed("7"))
        self.pushButton_8.clicked.connect(lambda: self.button_pressed("8"))
        self.pushButton_9.clicked.connect(lambda: self.button_pressed("9"))
        self.pushButton_10.clicked.connect(lambda: self.button_pressed("0"))
        self.pushButton_11.clicked.connect(lambda: self.button_pressed("."))
        self.pushButton_12.clicked.connect(self.calculate_result)
        self.pushButton_13.clicked.connect(lambda: self.button_pressed("+"))
        self.pushButton_14.clicked.connect(lambda: self.button_pressed("-"))
        self.pushButton_15.clicked.connect(lambda: self.button_pressed("*"))
        self.pushButton_16.clicked.connect(lambda: self.button_pressed("/"))
        self.pushButton_clear.clicked.connect(self.clear_input)

        # Variable to store current input
        self.current_input = ""

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_10.setText(_translate("MainWindow", "0"))
        self.pushButton_11.setText(_translate("MainWindow", "."))
        self.pushButton_12.setText(_translate("MainWindow", "="))
        self.pushButton_13.setText(_translate("MainWindow", "+"))
        self.pushButton_14.setText(_translate("MainWindow", "-"))
        self.pushButton_15.setText(_translate("MainWindow", "*"))
        self.pushButton_16.setText(_translate("MainWindow", "/"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))

    def button_pressed(self, button_value):
        self.current_input += button_value
        self.textBrowser.setText(self.current_input)

    def calculate_result(self):
        try:
            result = eval(self.current_input)
            self.textBrowser.setText(str(result))
            self.current_input = str(result)
        except Exception as e:
            self.textBrowser.setText("Error")
            self.current_input = ""

    def clear_input(self):
        self.current_input = ""
        self.textBrowser.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
