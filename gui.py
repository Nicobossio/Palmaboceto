#Manejo de la interfaz visual juntado con la entrada de datos

import tkinter as tk
from funcmenu import DataEntryForm
from data_display import DataDisplay
from database import Database

class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("CyberTracker Replica")

        self.db = Database("data.db")  # Replace "data.db" with your desired database file name

        self.data_entry_form = DataEntryForm(self.window, self.db)
        self.data_display = DataDisplay(self.window, self.db)

    def run(self):
        self.window.mainloop()

    def __del__(self):
        self.db.close()
