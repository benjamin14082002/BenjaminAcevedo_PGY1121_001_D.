from datetime import datetime
from random import randint
from random import choice

piso = [""] * 50  # Lista que representa los asientos del evento
precios = {"TipoA": 3800, "TipoB": 3000, "TipoC": 2800, "TipoD": 3500}  # Diccionario de precios por tipo de asiento
asistentes = []  # Lista para almacenar los datos de los asistentes
ganancias = {"TipoA": 0, "TipoB": 0, "TipoC": 0, "TipoD": 0}  # Diccionario para almacenar las ganancias por tipo de asiento

def comprar_piso():

    cantidad = int(input("Ingrese el piso comprar (1 a 10): "))
    if cantidad < 1 or cantidad > 10:
        print("La cantidad de entradas debe ser entre 1 y 10")
        return

    seleccionadas = []  # Lista para almacenar las ubicaciones seleccionadas

    for i in range(cantidad):
        mostrar_ubicaciones()
        ubicacion = int(input("Seleccione una ubicación disponible: "))

        if piso[ubicacion - 1] != "":
            print("La ubicación no está disponible")
            i -= 1
            return

        seleccionadas.append(ubicacion)

    rut = int(input("Ingrese el rut sin puntos ni guión y sin dígito verificador: "))
    if rut < 0 or rut > 99999999:
        rut = input("Rut inválido, ingrese solo los primeros 8 dígitos de su rut: ")

    nombreApellido = input("Ingrese su nombre completo: ")
    while nombreApellido == "":
        nombreApellido = input("Por favor ingrese un nombre: ")

    asistentes.append({
        "rut": rut,
        "nombreApellido": nombreApellido
    })

    for ubicacion in seleccionadas:
        if ubicacion <= 10:
            piso[ubicacion - 1] = "TipoA"
            ganancias["TipoA"] += precios["TipoA"]
        elif ubicacion >= 11 and ubicacion <= 30:
            piso[ubicacion - 1] = "TipoB"
            ganancias["TipoB"] += precios["TipoB"]
        elif ubicacion >= 31 and ubicacion <= 40:
            piso[ubicacion - 1] = "TipoC"
            ganancias["TipoC"] += precios["TipoC"]
        else:
            piso[ubicacion - 1] = "TipoD"
            ganancias["TipoD"] += precios["TipoD"]

    print("La operación se ha realizado correctamente")

def mostrar_ubicaciones():
    
    #muestra  los asientos disponibles y ocupados.
    
    for i in range(50):
        if i % 10 == 0:
            print()
        if piso[i] == "":
            print(i + 1, end=" ")
        else:
            print("X", end=" ")
    print()


def ver_listado_asistentes():
   
    asistentes.sort()  # Ordena la lista de asistentes por rut
    for i, rut in enumerate(asistentes):
        print(i + 1, rut)

def mostrar_ganancias():
    
    #muestra las ganancias totales para cada tipo de asiento y el monto total recaudado.
   
    total = 0  # Variable para almacenar el monto total recaudado

    for tipo, monto in ganancias.items():
        total += monto  # Suma el monto al total acumulado
        print(f"{tipo}: {monto}")

    print(f"Total: {total}")

def realizar_sorteo():
    
    #es una funcion para realizar un sorteo y selecciona un asistente al azar 
    
    seleccion = choice(asistentes)  # Selecciona al azar un asistente de la lista
    print(seleccion)


def salir():
    
    #Con esto se sale del programa y muestra un mensaje de despedida y la hora actual y el nombre del asistente registrado
   
    for nombreApellido in asistentes:
        print("Saliendo del programa. Adiós, ", nombreApellido["nombreApellido"], datetime.now())

def menu_principal():

    opcion = 0

    while opcion != 5:
        print("Menu principal")
        print("1. Comprar departamento")
        print("2. Mostrar ubicaciones disponibles")
        print("3. Ver listado de compradores")
        print("4. Mostrar ganancias totales")
        print("5. Salir")
        

        opcion = input("Ingrese la opción que desea: ")

        if opcion == "1":
            comprar_piso()
        elif opcion == "2":
            mostrar_ubicaciones()
        elif opcion == "3":
            ver_listado_asistentes()
        elif opcion == "4":
            mostrar_ganancias()
        elif opcion == "5":
            salir()
            break
        else:
            print("Opción inválida")

menu_principal()
