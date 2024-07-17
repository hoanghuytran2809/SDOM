import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow

    
def main():
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("Using PyQt6")
    main_window.setStyleSheet("background-color: white")
    main_window.setGeometry(0, 0, 400, 300)
    main_window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()