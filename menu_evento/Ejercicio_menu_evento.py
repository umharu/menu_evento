evento = ("iades", "2 de abril", "buenos aires", 25, [])

def registrar_partipantes(nombre, apellido, dni):
    if verificar_cupo():
        participante = (nombre, apellido, dni)
        evento[4].append(participante)
        print(f"Participante {nombre} {apellido} {dni} ha registrado correctamente")
    else:
        print("No hay cupos disponibles")

def verificar_cupo():
    return len(evento[4]) < evento[3]  

def listar_participantes():
    if evento[4]:
        for i , participante in enumerate(evento[4], start=1):
            print(f"{i}:{participante[0]} {participante[1]} - documento: {participante[2]}")
        else:
            print("No hay participantes registrados.")

def menu():
    while True:
        print("Menu del evento")
        print("1. Registrar participantes")
        print("2. Verificar cupo")
        print("3. Listar participantes")
        print("4. Salir")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            dni = input("Ingrese dni: ")
            registrar_partipantes(nombre, apellido, dni)
        elif opcion == "2":
            if verificar_cupo():
                print("Hay cupos")
            else:
                print("No hay cupos")
        elif opcion == "3":
                listar_participantes()
        elif opcion == "4":
            break
        else:
            print("Opcion incorrecta, seleccione del 1 al 4. ")
            
nuevo_menu = menu()