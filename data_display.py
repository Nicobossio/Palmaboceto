#Manera en la que se van a desplegar los datos
import tkinter as tk

class DataDisplay:
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db

        self.frame = tk.Frame(self.parent)
        self.frame.pack()

        self.data_listbox = tk.Listbox(self.frame, width=40)
        self.data_listbox.pack()

        self.populate_data()

    def populate_data(self):
        data = self.db.get_all_data()
        for item in data:
            self.data_listbox.insert(tk.END, item)
