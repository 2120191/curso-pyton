# return devuelve valores que podre aser uso
# crear una funcion que retorne el numero 10 y muestra por terminal si es par
# siempre que el valor que retorne mi funcion se utliza es mas sentencias u operaciones hacer uso de return
def diez():
    return 10
if diez ()%2==0:
    print("es par")
else:
    print("es impar")
    
# print solo muestra por terminal

# return cuandio queremos que nuestra fncon devuelva o retorne un tipo de dato o un tipo de dto estructurado

#creaar una funcion queme muestre el producto de dos numeros
def producto(a,b):
    return a*b
print(producto(4,8))
# crar una funcion  que me retorne una lista de tres numeros
def lista_numero():
    return [3,2,6]
# usaremos print cada vez que muestra funcion retorne un mensaje.
# craar yuna funcuoin que por parametro reciba un nombre y retorne un mensaje de bienvenida con el nombre.
def mensaje (nombre):
    print(f"hola, (nombre), bienvenido al chongo")
    mensaje("jose")

#crear una funcion que reciba por parametro una lista de numeros y me devuelve el numero menor, mostrar por terminal el valor por la funcion
def lista_numero():
    return(1,2,3,4)
print()
list 
lista=[4,3,6,78,7]
def min(l):



# crear una funcion que reciba como parametro el nombre y la edad de una persona mi funcion debera retornar un diccion con los datos, luego mostrar por terminal ewl valor de retorno de mi funcion
nombre=input("ingresa su nombre delincuente: ")
edad=int(input("ingresa su edad"))

nombre="abel"
edad=19
def persona(nom,edad):
    return {
    #   "nombre":nom
    #   "edad":edad
    }
    return dict(
        nombre=nom,
        edad=edad
    )
#print(persona(nombre,edad))


def suma(*args):
    args[0]=10
    print(args)
suma(4,7,8,5,2,4)


def suma(*args):
    nueva_lista=list(args)
    print(args)
suma(4,7,8,5,2,4)

# empaquetado y desempauquetado de argumentos dominales
def alumnos(**kwarsgs):
    kwarsgs["nombre"]="abel"
    print(kwarsgs)
alumnos(nombres="miguel",apellido="largo",edad=30)
## ejemplo de lambda
lambda:"hola"
print(lambda:"hola")


saludo=lambda:"hola"
print(saludo())



saludo=lambda n:f"hola, {n},{a}"
print(saludo)

#crear un programa anonimo qur reciba como parametro una lista de 5 numeros y retorne dos listas uno con los numeros pares y otra numeros impares
es_par= lambda x:x % 2 == 0
numeros=range(1,20)
numeros_pares=list(filter(es_par,numeros))
numeros_impares=list(filter(lambda x:not es_par(x),numeros))
print("lista de numeros pares:",numeros_pares)
print("lista de numeros impares:",numeros_impares) 


int (input())

def mensaje(m):
    print(m)

def pedir_nombre():
    nombre=input("ingresa tu nombre")
    return nombre
mensaje(pedir_nombre())
