#ENtrada  registro de los datos para la base de datos
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget

class DataEntryForm(QWidget):
    def __init__(self, db):
        super().__init__()

        self.db = db

        self.layout = QVBoxLayout(self)

        self.field1_label = QLabel("Identificacion:")
        self.layout.addWidget(self.field1_label)
        self.field1_entry = QLineEdit()
        self.layout.addWidget(self.field1_entry)

        self.field2_label = QLabel("Nombre:")
        self.layout.addWidget(self.field2_label)
        self.field2_entry = QLineEdit()
        self.layout.addWidget(self.field2_entry)

        self.field3_label = QLabel("Telefono:")
        self.layout.addWidget(self.field3_label)
        self.field3_entry = QLineEdit()
        self.layout.addWidget(self.field3_entry)

        self.submit_button = QPushButton("Enviar")
        self.submit_button.clicked.connect(self.submit_data)
        self.layout.addWidget(self.submit_button)

    def submit_data(self):
        field1 = self.field1_entry.text()
        field2 = self.field2_entry.text()
        field3 = self.field3_entry.text()

        self.db.insert_data(field1, field2, field3)

        self.field1_entry.clear()
        self.field2_entry.clear()
        self.field3_entry.clear()
