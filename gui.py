from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton
from funcmenu import DataEntryForm
from data_display import DataDisplay
from database import Database
from data_viewer import get_data
import csv

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App")

        self.db = Database("data.db")  # Reemplaza "data.db" con el nombre de archivo de base de datos deseado

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.data_entry_form = DataEntryForm(self.db)
        self.data_display = DataDisplay(self.db)

        self.layout.addWidget(self.data_entry_form)
        self.layout.addWidget(self.data_display)

        self.view_data_button = QPushButton("Ver Datos")
        self.view_data_button.clicked.connect(self.view_data)
        self.layout.addWidget(self.view_data_button)

    def view_data(self):
        data = get_data()
        self.export_to_excel(data)
        # Resto del código para mostrar los datos en la interfaz

    def export_to_excel(self, data):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Identificacion', 'Nombre', 'Telefono'])
            writer.writerows(data)

class GUI:
    def __init__(self):
        # Resto del código de inicialización de la GUI

        def view_data(self):
            # Resto del código para obtener los datos y llamar a MainWindow.export_to_excel()
            pass
