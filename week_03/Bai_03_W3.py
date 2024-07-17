from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QAction, QMessageBox, QVBoxLayout, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu Example")
        self.setGeometry(100, 100, 600, 400)

        # Main widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout(self.central_widget)

        # Example label
        self.label = QLabel("Select a menu item", self)
        self.layout.addWidget(self.label)

        # Menu bar
        self.menu_bar = self.menuBar()

        # File menu
        self.file_menu = self.menu_bar.addMenu("File")

        # Edit menu
        self.edit_menu = self.menu_bar.addMenu("Edit")

        # Help menu
        self.help_menu = self.menu_bar.addMenu("Help")

        # Adding actions to File menu
        self.add_action(self.file_menu, "New", "New selected")
        self.add_action(self.file_menu, "Open", "Open selected")
        self.add_action(self.file_menu, "Save", "Save selected")
        self.add_action(self.file_menu, "Exit", "Exit selected", self.close)

        # Adding actions to Edit menu
        self.add_action(self.edit_menu, "Cut", "Cut selected")
        self.add_action(self.edit_menu, "Copy", "Copy selected")
        self.add_action(self.edit_menu, "Paste", "Paste selected")

        # Adding actions to Help menu
        self.add_action(self.help_menu, "About", "About selected")

    def add_action(self, menu, action_name, message, triggered_action=None):
        action = QAction(action_name, self)
        if triggered_action:
            action.triggered.connect(triggered_action)
        else:
            action.triggered.connect(lambda: self.show_message(message))
        menu.addAction(action)

    def show_message(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Menu Selection")
        msg_box.setText(message)
        msg_box.exec()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
