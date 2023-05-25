#Se importa las funciones del menu anterior asi creando un espacio en cache
from funcmenu import agregar_proyecto, mostrar_proyectos, borrar_proyecto, agregar_pestanas, mostrar_pestanas


#Se muestra el menu con el que vamos a trabajar.
def mostrar_menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar proyecto")
        print("2. Mostrar proyectos")
        print("3. Agregar ventanas")
        print("4. Borrar proyectos")
        print("5. Mostrar ventanas y atributos")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_proyecto()
        elif opcion == "2":
            mostrar_proyectos()
        elif opcion == "3":
            agregar_pestanas()
        elif opcion == "4":
            borrar_proyecto
        elif opcion == "5":
            mostrar_pestanas()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

mostrar_menu()