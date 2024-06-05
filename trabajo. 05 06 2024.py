
# Diccionario para almacenar la información de los vehículos
vehiculos = {}

# Función para ver la lista de autos
def ver_lista_autos():
    if vehiculos:
        for id, info in vehiculos.items():
            print(f"ID: {id}, Marca: {info['marca']}, Modelo: {info['modelo']}, Año: {info['año']}, Precio: {info['precio']}")
    else:
        print("No hay vehículos en la lista.")

# Función para actualizar la lista de autos
def actualizar_lista_auto():
    ver_lista_autos()
    id_actualizar = int(input("Ingrese el ID del vehículo que desea actualizar: "))
    if id_actualizar in vehiculos:
        nuevo_precio = float(input("Ingrese el nuevo precio del vehículo: "))
        vehiculos[id_actualizar]["precio"] = nuevo_precio
        print("Lista de autos actualizada.")
    else:
        print("ID de vehículo no encontrado.")

# Función para agregar un nuevo vehículo
def agregar_nuevo_auto():
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    año = int(input("Ingrese el año del vehículo: "))
    precio = float(input("Ingrese el precio del vehículo: "))
    
    nuevo_id = max(vehiculos.keys(), default=0) + 1
    vehiculos[nuevo_id] = {"marca": marca, "modelo": modelo, "año": año, "precio": precio}
    print("Nuevo vehículo agregado.")

# Menú de opciones
while True:
    print("\nMenú de opciones:")
    print("1. Ver lista de autos")
    print("2. Actualizar lista de autos")
    print("3. Agregar un nuevo vehículo")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ver_lista_autos()
    elif opcion == "2":
        actualizar_lista_auto()
    elif opcion == "3":
        agregar_nuevo_auto()
    elif opcion == "4":
        print("Saliendo del sistema.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")



# crear una lista de numeros enteros del siguiente texto

texto="1,4,8,9,6"
convertir=texto.split(",")
print(convertir)


# texto="1,4,8,9,6"
# nueva_lista=[]
# for n in texto.split(","):
#    nueva_lista.append(n)
# print(nueva_lista)
# aplicando la tecnica vlc valor bucle y condicion
texto="1,4,8,9,6"
nueva_lista=[int(n) for n in texto.split(",") if int (n)%2==0]
print(nueva_lista)

# diccionarios por comprension
lista_amigos=["abel","anthony","edith","rut"]
diccionario=[]
for _,v in enumerate(lista_amigos):
    diccionario[v]=len(v)
print(diccionario)

# aplicando el vlc
lista_amigos=["abel","anthony","edith","rut"]
diccionario=[amigos:len(amigo)for amigo in lista_amigos]
print(diccionario)



lista_numero=("0,100")
def es_primo(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+5):
        if num %i== 0:
            return False
        return True
numeros_primos={num: "primo" for num in range(2, 100)if es_primo(num)}
primeros_20_numeros=dict(list(numeros_primos.items())[:20])
print(primeros_20_numeros)


