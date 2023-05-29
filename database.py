#Conexion con la base de datos, aca se usa SQL para la base de datos

import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                field1 TEXT,
                field2 TEXT,
                field3 INTEGER
            )
        """)
        self.connection.commit()

    def insert_data(self, field1, field2, field3):
        self.cursor.execute("""
            INSERT INTO data (field1, field2, field3)
            VALUES (?, ?, ?)
        """, (field1, field2, field3))
        self.connection.commit()

    def get_all_data(self):
        self.cursor.execute("SELECT * FROM data")
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
