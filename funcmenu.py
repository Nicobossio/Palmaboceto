#Entrada de datos
#Este arcivo maneja como se manejan los datos para la base de datos
import tkinter as tk

class DataEntryForm:
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db

        self.frame = tk.Frame(self.parent)
        self.frame.pack()

        self.field1_label = tk.Label(self.frame, text="Field 1:")
        self.field1_label.pack()
        self.field1_entry = tk.Entry(self.frame)
        self.field1_entry.pack()

        self.field2_label = tk.Label(self.frame, text="Field 2:")
        self.field2_label.pack()
        self.field2_entry = tk.Entry(self.frame)
        self.field2_entry.pack()

        self.field3_label = tk.Label(self.frame, text="Field 3:")
        self.field3_label.pack()
        self.field3_entry = tk.Entry(self.frame)
        self.field3_entry.pack()

        self.submit_button = tk.Button(self.frame, text="Submit", command=self.submit_data)
        self.submit_button.pack()

    def submit_data(self):
        field1 = self.field1_entry.get()
        field2 = self.field2_entry.get()
        field3 = int(self.field3_entry.get())

        self.db.insert_data(field1, field2, field3)

        self.field1_entry.delete(0, tk.END)
        self.field2_entry.delete(0, tk.END)
        self.field3_entry.delete(0, tk.END)
