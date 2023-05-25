#Se crea una lista para poder guardar los proyectos
proyectos = []


#Esto permitira al usuario, crear y agregar el proyecto
def agregar_proyecto():
    nombre = input("Ingrese el nombre del proyecto: ")
    proyectos.append(nombre)#Anade a la lista el nombre del proyecto
    print("Proyecto agregado con éxito.")


#En este caso el muestra cuantos proyectis tiene cada quien
def mostrar_proyectos():
    if len(proyectos) == 0:
        print("No hay proyectos disponibles.")
    else:
        print("Proyectos:")
        for proyecto in proyectos:
            print(proyecto)
            
#Aca se define la funcion para el borrado de los proyectos


#Se muestra el menu en donde va a uno a mirar que proyecttos tienen.
def mostrar_menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar proyecto")
        print("2. Mostrar proyectos")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_proyecto()
        elif opcion == "2":
            mostrar_proyectos()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el menú
mostrar_menu()
