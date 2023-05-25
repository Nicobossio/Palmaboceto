#Se crea una lista para poder guardar los proyectos
proyectos = []


#Esto permitira al usuario, crear y agregar el proyecto
def agregar_proyecto():
    nombre = input("Ingrese el nombre del proyecto: ")
    proyectos.append({"nombre": nombre, "pestanas": []})
    print("Proyecto agregado con éxito.")


#Muestra los proyectos en los cuales se va a trabajar
def mostrar_proyectos():
    if len(proyectos) == 0:
        print("No hay proyectos disponibles.")
    else:
        print("Proyectos:")
        for indice, proyecto in enumerate(proyectos):
            print(f"{indice+1}. {proyecto['nombre']}")



#Funcion para borrar los proyectos
def borrar_proyecto():
    if len(proyectos) == 0:
        print("No hay proyectos disponibles para borrar.")
    else:
        print("Proyectos:")
        for indice, proyecto in enumerate(proyectos):
            print(f"{indice+1}. {proyecto['nombre']}")
        
        while True:
            opcion = input("Ingrese el número del proyecto que desea borrar (0 para cancelar): ")
            if opcion.isdigit():
                indice = int(opcion) - 1
                if indice >= 0 and indice < len(proyectos):
                    proyecto_borrado = proyectos.pop(indice)
                    print(f"Proyecto '{proyecto_borrado['nombre']}' borrado con éxito.")
                elif indice == -1:
                    print("Operación cancelada.")
                else:
                    print("Índice inválido. Por favor, seleccione un número válido.")
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")
                continue
            
            opcion_continuar = input("¿Desea borrar otro proyecto? (s/n): ")
            if opcion_continuar.lower() != "s":
                break


#En este caso se crea una funcion para poder anadir unas pestanas a las cuales le vamos a meter atributos
def agregar_pestanas():
    if len(proyectos) == 0:
        print("No hay proyectos disponibles para agregar pestañas.")
    else:
        print("Proyectos:")
        for indice, proyecto in enumerate(proyectos):
            print(f"{indice+1}. {proyecto['nombre']}")
        
        while True:
            opcion = input("Ingrese el número del proyecto al que desea agregar pestañas (0 para cancelar): ")
            if opcion.isdigit():
                indice_proyecto = int(opcion) - 1
                if indice_proyecto >= 0 and indice_proyecto < len(proyectos):
                    proyecto = proyectos[indice_proyecto]
                    while True:
                        nombre_pestaña = input("Ingrese el nombre de la pestaña (0 para cancelar): ")
                        if nombre_pestaña == "0":
                            print("Operación cancelada.")
                            break
                        atributos = []
                        while True:
                            atributo = input("Ingrese un atributo para la pestaña (0 para terminar): ")
                            if atributo == "0":
                                break
                            atributos.append(atributo)
                        
                        proyecto["pestanas"].append({"nombre": nombre_pestaña, "atributos": atributos})
                        print("Pestaña agregada con éxito.")
                        
                        opcion_continuar = input("¿Desea agregar otra pestaña? (s/n): ")
                        if opcion_continuar.lower() != "s":
                            break
                elif indice_proyecto == -1:
                    print("Operación cancelada.")
                    break
                else:
                    print("Índice inválido. Por favor, seleccione un número válido.")
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")
                continue
            
            opcion_continuar = input("¿Desea agregar pestañas a otro proyecto? (s/n): ")
            if opcion_continuar.lower() != "s":
                break
                
                

#Esta funcion me ayuda a definir como se pueden mostrar las pestanas
def mostrar_pestanas():
   def mostrar_pestanas():
    if len(proyectos) == 0:
        print("No hay proyectos disponibles.")
    else:
        print("Proyectos:")
        for indice, proyecto in enumerate(proyectos):
            print(f"{indice+1}. {proyecto['nombre']}")
        
        while True:
            opcion = input("Ingrese el número del proyecto que desea ver/editar las pestañas (0 para cancelar): ")
            if opcion.isdigit():
                indice_proyecto = int(opcion) - 1
                if indice_proyecto >= 0 and indice_proyecto < len(proyectos):
                    proyecto = proyectos[indice_proyecto]
                    print(f"Pestañas del proyecto '{proyecto['nombre']}':")
                    pestañas = proyecto['pestanas']
                    if len(pestañas) == 0:
                        print("No hay pestañas disponibles.")
                    else:
                        for indice, pestaña in enumerate(pestañas):
                            print(f"{indice+1}. Pestaña: {pestaña['nombre']}")
                        
                        opcion_pestaña = input("Ingrese el número de la pestaña que desea editar (0 para cancelar): ")
                        if opcion_pestaña.isdigit():
                            indice_pestaña = int(opcion_pestaña) - 1
                            if indice_pestaña >= 0 and indice_pestaña < len(pestañas):
                                pestaña = pestañas[indice_pestaña]
                                print(f"Atributos de la pestaña '{pestaña['nombre']}':")
                                atributos = pestaña['atributos']
                                if len(atributos) == 0:
                                    print("No hay atributos disponibles.")
                                else:
                                    for indice, atributo in enumerate(atributos):
                                        print(f"{indice+1}. {atributo}")
                                    
                                    opcion_atributo = input("Ingrese el número del atributo que desea editar (0 para cancelar): ")
                                    if opcion_atributo.isdigit():
                                        indice_atributo = int(opcion_atributo) - 1
                                        if indice_atributo >= 0 and indice_atributo < len(atributos):
                                            nuevo_atributo = input("Ingrese el nuevo valor para el atributo: ")
                                            atributos[indice_atributo] = nuevo_atributo
                                            print("Atributo editado con éxito.")
                                        elif indice_atributo == -1:
                                            print("Operación cancelada.")
                                            break
                                        else:
                                            print("Índice inválido. Por favor, seleccione un número válido.")
                                    else:
                                        print("Opción inválida. Por favor, ingrese un número válido.")
                                        continue
                            elif indice_pestaña == -1:
                                print("Operación cancelada.")
                                break
                            else:
                                print("Índice inválido. Por favor, seleccione un número válido.")
                        else:
                            print("Opción inválida. Por favor, ingrese un número válido.")
                            continue
                elif indice_proyecto == -1:
                    print("Operación cancelada.")
                    break
                else:
                    print("Índice inválido. Por favor, seleccione un número válido.")
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")
                continue
            
            opcion_continuar = input("¿Desea ver/editar las pestañas de otro proyecto? (s/n): ")
            if opcion_continuar.lower() != "s":
                break