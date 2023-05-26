#Librerias importadas para la interfaz visual
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

# Se crea la clase de la ventana principal
class MenuVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú")
        self.setup_ui()

    def setup_ui(self):
        # Se crea el diseño vertical
        layout = QVBoxLayout()

        # Se crean los botones del menú
        btn_agregar_proyecto = QPushButton("Agregar proyecto")
        btn_mostrar_proyectos = QPushButton("Mostrar proyectos")
        btn_agregar_ventanas = QPushButton("Agregar ventanas")
        btn_borrar_proyectos = QPushButton("Borrar proyectos")
        btn_mostrar_ventanas = QPushButton("Mostrar ventanas y atributos")
        btn_salir = QPushButton("Salir")

        # Se conectan los botones con sus respectivas funciones
        btn_agregar_proyecto.clicked.connect(agregar_proyecto)
        btn_mostrar_proyectos.clicked.connect(mostrar_proyectos)
        btn_agregar_ventanas.clicked.connect(agregar_ventanas)
        btn_borrar_proyectos.clicked.connect(borrar_proyectos)
        btn_mostrar_ventanas.clicked.connect(mostrar_ventanas)
        btn_salir.clicked.connect(self.close)

        # Se agregan los botones al diseño
        layout.addWidget(btn_agregar_proyecto)
        layout.addWidget(btn_mostrar_proyectos)
        layout.addWidget(btn_agregar_ventanas)
        layout.addWidget(btn_borrar_proyectos)
        layout.addWidget(btn_mostrar_ventanas)
        layout.addWidget(btn_salir)

        # Se establece el diseño en la ventana principal
        self.setLayout(layout)


# Funciones del menú
def agregar_proyecto():
    print("Agregar proyecto")

def mostrar_proyectos():
    print("Mostrar proyectos")

def agregar_ventanas():
    print("Agregar ventanas")

def borrar_proyectos():
    print("Borrar proyectos")

def mostrar_ventanas():
    print("Mostrar ventanas y atributos")


# Función principal para ejecutar la aplicación
def main():
    app = QApplication(sys.argv)
    ventana = MenuVentana()
    ventana.show()
    sys.exit(app.exec_())

# Ejecuta la aplicación
if __name__ == "__main__":
    main()
