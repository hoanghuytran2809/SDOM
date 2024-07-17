import sys
from PySide6.QtCore import QTime, QTimer, Slot, Qt
from PySide6.QtGui import QPalette, QPixmap, QBrush
from PySide6.QtWidgets import QApplication, QLCDNumber, QWidget, QVBoxLayout

class DigitalClock(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Thiết lập layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Thiết lập QLCDNumber
        self.lcd = QLCDNumber()
        self.lcd.setSegmentStyle(QLCDNumber.Filled)
        self.lcd.setDigitCount(8)
        layout.addWidget(self.lcd)

        # Thiết lập hình nền
        self.set_background("img_01.jpg")

        # Thiết lập timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

        self.show_time()

        self.setWindowTitle("Digital Clock")
        self.resize(250, 60)

    def set_background(self, image_path):
        palette = QPalette()
        pixmap = QPixmap(image_path)
        
        # Đảm bảo hình ảnh được thay đổi kích thước để phù hợp với kích thước cửa sổ
        scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio)
        brush = QBrush(scaled_pixmap)
        palette.setBrush(QPalette.Window, brush)
        
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    @Slot()
    def show_time(self):
        time = QTime.currentTime()
        text = time.toString("hh:mm:ss")

        # Hiệu ứng nhấp nháy
        if (time.second() % 2) == 0:
            text = text.replace(":", " ")

        self.lcd.display(text)

    def resizeEvent(self, event):
        # Cập nhật hình nền khi thay đổi kích thước cửa sổ
        self.set_background("img_01.jpg")
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec())
