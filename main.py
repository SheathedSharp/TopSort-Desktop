from core.main_window import MainWindow
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("statics/logo.png"))
    main_window = MainWindow()
    main_window.ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
