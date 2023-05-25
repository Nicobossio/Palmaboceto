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

#En este caso se crea una funcion para poder anadir unas pestanas a las cuales le vamos a meter atributos
def agregar_pestanas():
    # Mostrar lista de proyectos
    print("Lista de proyectos:")
    for indice, proyecto in enumerate(proyectos):
        print(f"{indice+1}. {proyecto['nombre']}")

    # Seleccionar un proyecto
    seleccion = input("Seleccione el número de proyecto al que desea agregar una pestaña (0 para salir): ")
    if seleccion == '0':
        return

    # Verificar si el número seleccionado es válido
    try:
        indice = int(seleccion) - 1
        if indice < 0 or indice >= len(proyectos):
            print("Número de proyecto inválido.")
            return
    except ValueError:
        print("Ingrese un número válido.")
        return

    proyecto = proyectos[indice]

    # Agregar una nueva pestaña
    nombre_pestaña = input("Ingrese el nombre de la pestaña: ")
    atributo_pestaña = input("Ingrese el atributo de la pestaña: ")

    # Crear un diccionario para representar la pestaña
    pestaña = {'nombre': nombre_pestaña, 'atributo': atributo_pestaña}

    # Agregar la pestaña al proyecto
    proyecto['pestanas'].append(pestaña)

    print("Pestaña agregada exitosamente.")


#Se muestra el menu en donde va a uno a mirar que proyecttos tienen.
def mostrar_menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar proyecto")
        print("2. Mostrar proyectos")
        print("3. Agregar pestanas")
        print("4. Borrar proyectos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_proyecto()
        elif opcion == "2":
            mostrar_proyectos()
        elif opcion == "3":
            agregar_pestanas()
        elif opcion == "4":
            borrar_proyecto()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el menú
mostrar_menu()
