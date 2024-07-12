# practicando pylint
nombre_alumno:str="miguel"

def suma(a:int,b:int)->int:
    """funcion para sumar dos numeros"""
    return a+b
print(suma(4,7))
         
def resta(a,b):
     """funcion para resta dos numeros"""
     return a-b
def producto(a,b):
     """funcion de producto"""
     return a*b
# importacion directa

import operaciones
suma:int=operaciones,suma(7,8)
msj:str=operaciones.mensaje
print(suma)

import operaciones
suma:int=operaciones,suma(7,8)
msj:str=f"{operaciones.mensaje},
como estas"
print(suma)