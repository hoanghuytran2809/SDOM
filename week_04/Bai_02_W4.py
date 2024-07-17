import sys
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QColorDialog

class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: white;")  # Đặt màu nền là trắng
        self.drawing = False
        self.last_point = QPoint()
        self.pen_color = QColor('white')
        self.points = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(self.pen_color, 2, Qt.PenStyle.SolidLine))

        if self.points:
            for i in range(len(self.points) - 1):
                painter.drawLine(self.points[i], self.points[i + 1])

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.last_point = event.pos()
            self.points.append(self.last_point)

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.points.append(event.pos())
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False

    def clear_canvas(self):
        self.points = []
        self.update()

    def change_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.pen_color = color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.canvas = Canvas()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Drawing Application")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.layout.addWidget(self.canvas)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.clicked.connect(self.canvas.clear_canvas)
        self.layout.addWidget(self.clear_button)

        self.color_button = QPushButton("Change Color", self)
        self.color_button.clicked.connect(self.canvas.change_color)
        self.layout.addWidget(self.color_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
