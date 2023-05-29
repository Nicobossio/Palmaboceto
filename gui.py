#Se anade el pqt5 para integrarlo con el primer menu
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from funcmenu import DataEntryForm
from data_display import DataDisplay
from database import Database

class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CyberTracker Replica")

        self.db = Database("data.db")  # Replace "data.db" with your desired database file name

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.data_entry_form = DataEntryForm(self.db)
        self.data_display = DataDisplay(self.db)

        self.layout.addWidget(self.data_entry_form)
        self.layout.addWidget(self.data_display)

        self.show()

    def __del__(self):
        self.db.close()
