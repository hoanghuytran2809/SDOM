from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QVBoxLayout, QWidget

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Notepad")
        self.setGeometry(100, 100, 600, 400)

        # Main widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.central_widget.setStyleSheet("background-color: white; color: black;")

        # Layout
        self.layout = QVBoxLayout(self.central_widget)

        # Text edit widget
        self.text_edit = QTextEdit(self)
        self.text_edit.setStyleSheet("background-color: white; color: black;")
        self.text_edit.textChanged.connect(self.update_character_count)
        self.layout.addWidget(self.text_edit)

        # Character count label
        self.char_count_label = QLabel("Characters: 0", self)
        self.char_count_label.setStyleSheet("color: black;")
        self.layout.addWidget(self.char_count_label)

    def update_character_count(self):
        text = self.text_edit.toPlainText()
        char_count = len(text)
        self.char_count_label.setText(f"Characters: {char_count}")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    notepad = Notepad()
    notepad.show()
    sys.exit(app.exec())
