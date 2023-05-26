#Librerias para la interfaz visual
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox


# Se crea una ventana para agregar proyectos
class AgregarProyectoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Agregar Proyecto")
        self.layout = QVBoxLayout()
        self.label_nombre = QLabel("Nombre del proyecto:")
        self.input_nombre = QLineEdit()
        self.boton_agregar = QPushButton("Agregar")
        self.boton_agregar.clicked.connect(self.agregar_proyecto)
        self.layout.addWidget(self.label_nombre)
        self.layout.addWidget(self.input_nombre)
        self.layout.addWidget(self.boton_agregar)
        self.setLayout(self.layout)

    def agregar_proyecto(self):
        nombre = self.input_nombre.text()
        if nombre:
            proyectos.append({"nombre": nombre, "pestanas": []})
            print("Proyecto agregado con éxito.")
            self.close()


# Se crea una ventana para agregar pestañas
class AgregarPestanasDialog(QDialog):
    def __init__(self, proyectos, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Agregar Pestañas")
        self.layout = QVBoxLayout()
        self.label_proyecto = QLabel("Seleccione un proyecto:")
        self.combo_proyecto = QComboBox()
        self.combo_proyecto.addItems([proyecto["nombre"] for proyecto in proyectos])
        self.label_nombre = QLabel("Nombre de la pestaña:")
        self.input_nombre = QLineEdit()
        self.boton_agregar = QPushButton("Agregar")
        self.boton_agregar.clicked.connect(self.agregar_pestanas)
        self.layout.addWidget(self.label_proyecto)
        self.layout.addWidget(self.combo_proyecto)
        self.layout.addWidget(self.label_nombre)
        self.layout.addWidget(self.input_nombre)
        self.layout.addWidget(self.boton_agregar)
        self.setLayout(self.layout)

    def agregar_pestanas(self):
        indice_proyecto = self.combo_proyecto.currentIndex()
        proyecto = proyectos[indice_proyecto]
        nombre_pestaña = self.input_nombre.text()
        if nombre_pestaña:
            atributos = []
            agregar_atributos_dialog = AgregarAtributosDialog(atributos, self)
            agregar_atributos_dialog.exec_()
            proyecto["pestanas"].append({"nombre": nombre_pestaña, "atributos": atributos})
            print("Pestaña agregada con éxito.")
            self.close()


# Se crea una ventana para agregar atributos
class AgregarAtributosDialog(QDialog):
    def __init__(self, atributos, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Agregar Atributos")
        self.layout = QVBoxLayout()
        self.label_atributo = QLabel("Ingrese un atributo (0 para terminar):")
        self.input_atributo = QLineEdit()
        self.boton_agregar = QPushButton("Agregar")
        self.boton_agregar.clicked.connect(self.agregar_atributo)
        self.layout.addWidget(self.label_atributo)
        self.layout.addWidget(self.input_atributo)
        self.layout.addWidget(self.boton_agregar)
        self.setLayout(self.layout)
        self.atributos = atributos

    def agregar_atributo(self):
        atributo = self.input_atributo.text()
        if atributo != "0":
            self.atributos.append(atributo)
            self.input_atributo.clear()
        else:
            self.close()


# Se crea una ventana principal con botones para realizar las diferentes acciones del menú
class MenuVentana(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Menu")
        self.setGeometry(100, 100, 300, 200)

        self.boton_agregar_proyecto = QPushButton("Agregar Proyecto", self)
        self.boton_agregar_proyecto.setGeometry(50, 50, 200, 30)
        self.boton_agregar_proyecto.clicked.connect(self.mostrar_agregar_proyecto)

        self.boton_agregar_pestanas = QPushButton("Agregar Pestañas", self)
        self.boton_agregar_pestanas.setGeometry(50, 100, 200, 30)
        self.boton_agregar_pestanas.clicked.connect(self.mostrar_agregar_pestanas)

        self.boton_mostrar_proyectos = QPushButton("Mostrar Proyectos", self)
        self.boton_mostrar_proyectos.setGeometry(50, 150, 200, 30)
        self.boton_mostrar_proyectos.clicked.connect(self.mostrar_proyectos)

    def mostrar_agregar_proyecto(self):
        agregar_proyecto_dialog = AgregarProyectoDialog(self)
        agregar_proyecto_dialog.exec_()

    def mostrar_agregar_pestanas(self):
        if len(proyectos) == 0:
            print("No hay proyectos disponibles para agregar pestañas.")
        else:
            agregar_pestanas_dialog = AgregarPestanasDialog(proyectos, self)
            agregar_pestanas_dialog.exec_()

    def mostrar_proyectos(self):
        if len(proyectos) == 0:
            print("No hay proyectos disponibles.")
        else:
            print("Proyectos:")
            for indice, proyecto in enumerate(proyectos):
                print(f"{indice + 1}. {proyecto['nombre']}")


# Se crea una lista para poder guardar los proyectos
proyectos = []


# Se crea la aplicación y se muestra la ventana principal
app = QApplication(sys.argv)
menu = MenuVentana()
menu.show()

# Se ejecuta la aplicación
sys.exit(app.exec_())
