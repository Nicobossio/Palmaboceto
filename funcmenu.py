#Librerias para la interfaz visual
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit


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


# Se crea una ventana para mostrar los proyectos y seleccionar uno para ver sus atributos
class MostrarProyectosDialog(QDialog):
    def __init__(self, proyectos, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Mostrar Proyectos")
        self.layout = QVBoxLayout()
        self.label_proyectos = QLabel("Proyectos:")
        self.text_proyectos = QTextEdit()
        self.text_proyectos.setReadOnly(True)
        self.boton_seleccionar = QPushButton("Seleccionar Proyecto")
        self.boton_seleccionar.clicked.connect(self.mostrar_atributos)
        self.layout.addWidget(self.label_proyectos)
        self.layout.addWidget(self.text_proyectos)
        self.layout.addWidget(self.boton_seleccionar)
        self.setLayout(self.layout)
        self.proyectos = proyectos
        self.mostrar_lista_proyectos()

    def mostrar_lista_proyectos(self):
        lista_proyectos = "\n".join([f"{indice + 1}. {proyecto['nombre']}" for indice, proyecto in enumerate(self.proyectos)])
        self.text_proyectos.setText(lista_proyectos)

    def mostrar_atributos(self):
        indice_proyecto = self.text_proyectos.textCursor().blockNumber()
        proyecto = self.proyectos[indice_proyecto]
        mostrar_atributos_dialog = MostrarAtributosDialog(proyecto)
        mostrar_atributos_dialog.exec_()


# Se crea una ventana para mostrar los atributos de un proyecto
class MostrarAtributosDialog(QDialog):
    def __init__(self, proyecto, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Mostrar Atributos")
        self.layout = QVBoxLayout()
        self.label_atributos = QLabel(f"Atributos del proyecto '{proyecto['nombre']}':")
        self.text_atributos = QTextEdit()
        self.text_atributos.setReadOnly(True)
        self.layout.addWidget(self.label_atributos)
        self.layout.addWidget(self.text_atributos)
        self.setLayout(self.layout)
        self.mostrar_lista_atributos(proyecto)

    def mostrar_lista_atributos(self, proyecto):
        lista_atributos = "\n".join([f"{indice + 1}. {atributo}" for indice, atributo in enumerate(proyecto['atributos'])])
        self.text_atributos.setText(lista_atributos)


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
        if len(proyectos) > 0:
            agregar_pestanas_dialog = AgregarPestanasDialog(proyectos, self)
            agregar_pestanas_dialog.exec_()
        else:
            print("No hay proyectos para agregar pestañas.")

    def mostrar_proyectos(self):
        if len(proyectos) > 0:
            mostrar_proyectos_dialog = MostrarProyectosDialog(proyectos, self)
            mostrar_proyectos_dialog.exec_()
        else:
            print("No hay proyectos para mostrar.")


if __name__ == '__main__':
    proyectos = []

    app = QApplication(sys.argv)
    menu_ventana = MenuVentana()
    menu_ventana.show()
    sys.exit(app.exec_())
