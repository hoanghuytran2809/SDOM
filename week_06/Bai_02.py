from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Main layout
        self.mainLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")

        # Left sidebar layout
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        self.sidebar.setStyleSheet("background-color: #4682B4;")
        self.sidebar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sidebar.setObjectName("sidebar")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.sidebar)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")

        self.logoLabel = QtWidgets.QLabel(self.sidebar)
        self.logoLabel.setPixmap(QtGui.QPixmap("logo.png"))
        self.logoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.logoLabel.setObjectName("logoLabel")
        self.verticalLayout.addWidget(self.logoLabel)

        self.statusButton = QtWidgets.QPushButton("Status", self.sidebar)
        self.statusButton.setObjectName("statusButton")
        self.verticalLayout.addWidget(self.statusButton)

        self.updatesButton = QtWidgets.QPushButton("Updates", self.sidebar)
        self.updatesButton.setObjectName("updatesButton")
        self.verticalLayout.addWidget(self.updatesButton)

        self.settingsButton = QtWidgets.QPushButton("Settings", self.sidebar)
        self.settingsButton.setObjectName("settingsButton")
        self.verticalLayout.addWidget(self.settingsButton)

        self.shareFeedbackButton = QtWidgets.QPushButton("Share Feedback", self.sidebar)
        self.shareFeedbackButton.setObjectName("shareFeedbackButton")
        self.verticalLayout.addWidget(self.shareFeedbackButton)

        self.buyPremiumButton = QtWidgets.QPushButton("Buy Premium", self.sidebar)
        self.buyPremiumButton.setObjectName("buyPremiumButton")
        self.verticalLayout.addWidget(self.buyPremiumButton)

        self.helpButton = QtWidgets.QPushButton("Help", self.sidebar)
        self.helpButton.setObjectName("helpButton")
        self.verticalLayout.addWidget(self.helpButton)

        self.verticalLayout.addStretch()

        self.scanNowButton = QtWidgets.QPushButton("Scan Now", self.sidebar)
        self.scanNowButton.setStyleSheet("background-color: green; color: white;")
        self.scanNowButton.setObjectName("scanNowButton")
        self.verticalLayout.addWidget(self.scanNowButton)

        self.mainLayout.addWidget(self.sidebar)

        # Main content layout
        self.mainContent = QtWidgets.QFrame(self.centralwidget)
        self.mainContent.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mainContent.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mainContent.setObjectName("mainContent")

        self.verticalLayout2 = QtWidgets.QVBoxLayout(self.mainContent)
        self.verticalLayout2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout2.setSpacing(15)
        self.verticalLayout2.setObjectName("verticalLayout2")

        self.scanLabel = QtWidgets.QLabel("Scan", self.mainContent)
        self.scanLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.scanLabel.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.scanLabel.setObjectName("scanLabel")
        self.verticalLayout2.addWidget(self.scanLabel)

        self.descriptionLabel = QtWidgets.QLabel("Premium will be free forever. You just need to click button.", self.mainContent)
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.verticalLayout2.addWidget(self.descriptionLabel)

        self.buttonLayout = QtWidgets.QGridLayout()

        self.quickScanButton = QtWidgets.QPushButton("Quick Scan", self.mainContent)
        self.quickScanButton.setStyleSheet("background-color: magenta; color: white;")
        self.quickScanButton.setObjectName("quickScanButton")
        self.buttonLayout.addWidget(self.quickScanButton, 0, 0)

        self.webProtectionButton = QtWidgets.QPushButton("Web Protection", self.mainContent)
        self.webProtectionButton.setStyleSheet("background-color: magenta; color: white;")
        self.webProtectionButton.setObjectName("webProtectionButton")
        self.buttonLayout.addWidget(self.webProtectionButton, 0, 1)

        self.quarantineButton = QtWidgets.QPushButton("Quarantine", self.mainContent)
        self.quarantineButton.setStyleSheet("background-color: magenta; color: white;")
        self.quarantineButton.setObjectName("quarantineButton")
        self.buttonLayout.addWidget(self.quarantineButton, 1, 0)

        self.fullScanButton = QtWidgets.QPushButton("Full Scan", self.mainContent)
        self.fullScanButton.setStyleSheet("background-color: magenta; color: white;")
        self.fullScanButton.setObjectName("fullScanButton")
        self.buttonLayout.addWidget(self.fullScanButton, 1, 1)

        self.simpleUpdateButton = QtWidgets.QPushButton("Simple Update", self.mainContent)
        self.simpleUpdateButton.setStyleSheet("background-color: magenta; color: white;")
        self.simpleUpdateButton.setObjectName("simpleUpdateButton")
        self.buttonLayout.addWidget(self.simpleUpdateButton, 2, 0)

        self.verticalLayout2.addLayout(self.buttonLayout)

        self.premiumNoticeLabel = QtWidgets.QLabel("Get Premium to Enable: {Web Protection}, {Full Scan}, {Simple Update}", self.mainContent)
        self.premiumNoticeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.premiumNoticeLabel.setObjectName("premiumNoticeLabel")
        self.verticalLayout2.addWidget(self.premiumNoticeLabel)

        self.mainLayout.addWidget(self.mainContent)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to functions
        self.statusButton.clicked.connect(self.showStatus)
        self.updatesButton.clicked.connect(self.showUpdates)
        self.settingsButton.clicked.connect(self.showSettings)
        self.shareFeedbackButton.clicked.connect(self.shareFeedback)
        self.buyPremiumButton.clicked.connect(self.buyPremium)
        self.helpButton.clicked.connect(self.showHelp)
        self.scanNowButton.clicked.connect(self.scanNow)
        self.quickScanButton.clicked.connect(self.quickScan)
        self.webProtectionButton.clicked.connect(self.webProtection)
        self.quarantineButton.clicked.connect(self.quarantine)
        self.fullScanButton.clicked.connect(self.fullScan)
        self.simpleUpdateButton.clicked.connect(self.simpleUpdate)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Antivirus AtarBals"))

    def showStatus(self):
        self.showMessage("Status", "This is the status page.")

    def showUpdates(self):
        self.showMessage("Updates", "This is the updates page.")

    def showSettings(self):
        self.showMessage("Settings", "This is the settings page.")

    def shareFeedback(self):
        self.showMessage("Share Feedback", "This is the feedback page.")

    def buyPremium(self):
        self.showMessage("Buy Premium", "This is the buy premium page.")

    def showHelp(self):
        self.showMessage("Help", "This is the help page.")

    def scanNow(self):
        self.showMessage("Scan Now", "Scanning now...")

    def quickScan(self):
        self.showMessage("Quick Scan", "Performing a quick scan...")

    def webProtection(self):
        self.showMessage("Web Protection", "Enabling web protection...")

    def quarantine(self):
        self.showMessage("Quarantine", "Quarantining files...")

    def fullScan(self):
        self.showMessage("Full Scan", "Performing a full scan...")

    def simpleUpdate(self):
        self.showMessage("Simple Update", "Performing a simple update...")

    def showMessage(self, title, message):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
