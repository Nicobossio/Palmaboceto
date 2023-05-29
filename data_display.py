#Manera en la que se muestran los datos
from PyQt5.QtWidgets import QListWidget, QVBoxLayout, QWidget

class DataDisplay(QWidget):
    def __init__(self, db):
        super().__init__()

        self.db = db

        self.layout = QVBoxLayout(self)

        self.data_listbox = QListWidget()
        self.layout.addWidget(self.data_listbox)

        self.populate_data()

    def populate_data(self):
        data = self.db.get_all_data()
        for item in data:
            self.data_listbox.addItem(str(item))
