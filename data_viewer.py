import sqlite3
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget

class DataDisplay(QWidget):
    def __init__(self, db):
        super().__init__()

        self.db = db

        self.layout = QVBoxLayout(self)

        self.data_label = QLabel()
        self.layout.addWidget(self.data_label)

        self.populate_data()

    def populate_data(self):
        data = self.db.get_all_data()
        data_text = ""
        for item in data:
            data_text += str(item) + "\n"

        self.data_label.setText(data_text)
    


def get_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data_table")
    data = cursor.fetchall()
    conn.close()
    return data

