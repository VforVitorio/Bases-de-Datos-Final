import biblioteca as bl
from biblioteca import Avion, Pasaporte

aviones = []
opcion = 0

while opcion != 9:
    print("Menu de opciones:")
    print("1. Agregar avion")
    print("2. Eliminar avion")
    print("3. Agregar pasaporte a un avion")
    print("4. Eliminar pasaporte de un avion")
    print("5. Generar pasaportes aleatorios para un avion")
    print("6. Mostrar todos los aviones")
    print("7. Mostrar todos los pasajeros de un avion: ")
    print("8. Mostrar las restricciones de los pasajeros de un avion")
    print("9. Salir")
    opcion = int(input("Introduzca la opcion deseada: "))

    if opcion == 1:
        modelo = input("Introduzca el modelo del avion: ")
        origen = input("Introduzca el origen del avion: ")
        num_pasajeros = int(
            input("Introduzca el numero de pasajeros del avion: "))
        avion = Avion(modelo, origen, num_pasajeros)
        bl.agregar_avion_a_lista(aviones, avion)
        print("Avion agregado con exito.")
    elif opcion == 2:
        modelo = input("Introduzca el modelo del avion a eliminar: ")
        avion = bl.buscar_avion(aviones, modelo)
        if avion is not None:
            aviones.remove(avion)
            print("Avion eliminado con exito.")
        else:
            print("No se encontro el avion con el modelo especificado.")
    elif opcion == 3:
        modelo = input("Introduzca el modelo del avion: ")
        avion = bl.buscar_avion(aviones, modelo)
        if avion is not None:
            num_pasaporte = input("Introduzca el numero de pasaporte: ")
            nombre = input("Introduzca el nombre del pasajero: ")
            apellido = input("Introduzca el apellido del pasajero: ")
            nacionalidad = input("Introduzca la nacionalidad del pasajero: ")
            dni = input("Introduzca el DNI del pasajero: ")
            edad = int(input("Introduzca la edad del pasajero: "))
            sexo = input("Introduzca el sexo del pasajero: ")
            pasaporte = Pasaporte(num_pasaporte, nombre,
                                  apellido, nacionalidad, dni, edad, sexo)
            bl.agregar_pasaporte(avion, pasaporte)
            print("Pasaporte agregado con exito.")
        else:
            print("No se encontro el avion con el modelo especificado.")
    elif opcion == 4:
        modelo = input("Introduzca el modelo del avion: ")
        avion = bl.buscar_avion(aviones, modelo)
        if avion is not None:
            num_pasaporte = input(
                "Introduzca el número de pasaporte a eliminar: ")
            bl.eliminarPasaporte(avion, num_pasaporte)
            print("Pasaporte eliminado con exito.")
        else:
            print("No se encontro el avion con el modelo especificado.")
    elif opcion == 5:
        modelo = input("Introduzca el modelo del avion: ")
        num_pasaportes = int(
            input("Introduzca el numero de pasaportes aleatorios a generar: "))
        avion = bl.buscar_avion(aviones, modelo)
        if avion is not None:
            bl.GenRanPass(avion, num_pasaportes)
            print("Pasaportes aleatorios generados con exito.")
        else:
            print("No se encontro el avion con el modelo especificado.")
    elif opcion == 6:
        bl.mostrar_todos_los_aviones(aviones)
    elif opcion == 7:
        modelo = input("Ingrese el modelo del avion: ")
        avion = bl.buscar_avion(aviones, modelo)
        if avion is not None:
            bl.mostrar_pasajeros(avion.pasaportes, avion)
        else:
            print("No se encontro el avion con el modelo especificado.")
    elif opcion == 8:
        modelo = input("Ingrese el modelo del avion: ")
        avion = bl.buscar_avion(aviones, modelo)
        if avion is not None:
            bl.mostrar_restricciones(avion)
        else:
            print("No se encontro el avion con el modelo especificado.")
    elif opcion == 9:
        print("Saliendo del programa...")
