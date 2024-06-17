## crear una funcion que reciba por agumentos n numeros y retorne una lista con los numeros pares
def num_pares(*args):
    lista_pares=[]
    for n in args:
        if n%2==0:
            lista_pares.append(n)
    return [n for n in args if n%2==0]
print(num_pares(8,5,4,7,9,25,4,7,12))
#crear tres funciones para los siguientes casos
#caluclar el numero menor
#calcular el numero mayor
#calcular la suma de todos los numeros
#se le pasara por argumento n numeros
def list_num(*args):
    list_num=[]
    for n in args:
        if n<5:
            print("es menor")
        if n>5:
            print("es mayor")
        list_num.append(n)
    return [n for n in args]
print(list_num(4,5,6,7,7,7,8,9))



def min(*args):
    menor=args[0]
    for n in args:
        if n<menor:
            menor=n
    return menor
def max(*args):
    mayor=args[0]
    for n in args:
        if n>mayor:
            mayor=n
    return mayor
def sum(*args):
    suma=0
    for n in args:
        suma+=n
    return suma

valores=4,7,8,5,2,1
print(min(*valores))
print(max(*valores))
print(sum(*valores))

