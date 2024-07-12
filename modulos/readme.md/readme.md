# averiguar sobre modulos y paquetes en phyton
 ## Módulos
Un módulo es un archivo de Python cuyos objetos (funciones, clases, excepciones, etc.) pueden ser accedidos desde otro archivo. Se trata simplemente de una forma de organizar grandes códigos.

Consideremos, por ejemplo, un archivo aritmetica.py que contenga las siguientes definiciones.

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b
Podemos acceder a ellas desde otro archivo de Python ubicado en la misma ruta importando el módulo.

import aritmetica

print(aritmetica.sumar(7, 5))
Una sintaxis alternativa para importar objetos desde un módulo es la siguiente.

from aritmetica import sumar

print(sumar(7, 5))
## Paquetes
Un paquete es una carpeta que contiene varios módulos. Siguiendo el ejemplo anterior, podemos diseñar un paquete matematica creando una carpeta con la siguiente estructura.

matematica/
    |-- __init__.py
    |-- aritmetica.py
    |-- geometria.py
Debe contener siempre un archivo __init__.py (por el momento vacío) para que Python entienda que se trata de un paquete y no de una simple carpeta. Así, podemos acceder a alguno de los módulos del paquete de la siguiente manera.

import matematica.aritmetica

print(matematica.aritmetica.sumar(7, 5))
O bien de la siguiente.

from matematica import aritmetica
print(aritmetica.sumar(7, 5))
También, esta otra:
rom matematica.aritmetica import sumar
print(sumar(7, 5))

# diferencias entre modulos y pauqtes
# Una librería
 se define como una colección de cosas útiles relacionadas, en nuestro caso, funciones útiles relacionadas; por ejemplo, Necesito manejar valores de fecha y hora → uso la librería Moment.js con funciones específicas para trabajar fecha y hora, y me ahorror escribir ese código.
# Un módulo
 es una unidad de software que provee una función. Podemos exportar librerías como módulos para integrarlas a nuestro código, o crear módulos para dividir nuestro código en partes y que sea más fácil de manejar.
# Un paquete
 es un archivo o folder que puede contener uno o más módulos.
Una dependencia es una forma de decir “¡Hey! voy a usar código que pertenece a X módulo”, asegúrate de incluirlo (instalarlo).