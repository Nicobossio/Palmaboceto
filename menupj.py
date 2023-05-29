#Libreria visual para la interfa grafica
from gui import Application
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = Application()
    application.run()
    sys.exit(app.exec())
