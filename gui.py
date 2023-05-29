from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from funcmenu import DataEntryForm
from data_display import DataDisplay
from database import Database
import sys

class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.main_window = MainWindow()
        self.main_window.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CyberTracker Replica")

        self.db = Database("data.db")  # Reemplaza "data.db" con el nombre de archivo de base de datos deseado

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.data_entry_form = DataEntryForm(self.db)
        self.data_display = DataDisplay(self.db)

        self.layout.addWidget(self.data_entry_form)
        self.layout.addWidget(self.data_display)

    def closeEvent(self, event):
        self.db.close()

if __name__ == "__main__":
    app = Application(sys.argv)
    sys.exit(app.exec())
