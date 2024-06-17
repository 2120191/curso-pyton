return6# FUNCIONES
## concepto
matematicamentes una funcion e6s una operacion que toma una omas valores llamados `argumentos` y produce un valor denominados `resultado`.
>¨[!note]
> todos los lenguajes de programacion tiene funciones incorporadas(`funcuiones internas`), y funciones creadas por el usuario (`funciones exrternas`)

en programacion una funcion es un subprograma, es una estructura que nos permite agrupar codigo yy sus principales son :
-`no repetir` feacgementos de codigos
-`REUTILIZAR` el codigo enh distintos escenarios
## estructura de una funcion
una dfuncion viene `definida` por un `nombre`,k sus `parametros` y su valor de `retorno`.
una vez creada la funcion podemos solicitar su ejecucucion `invocando` la funcion por su `nombre`
## definir una funcion phyton
para definir una funcion en phyton primero utlizaremos la palabra reservada `def` seguida por el `nombre` de la funcion. a continuacion especificaremos los `parametros` con `()` si es una funcion sin parametros, `(a)` si es una funcion con parametros, sin tuviera mas de un parametros iran separadas por `,`, finalizaremos la linea con `:`, en la siguiente linea sin olvidar el identado, comenzara el cuerpo de la funcion(micrioprograma)que puede contener uno o mas sentencias finalmente devera `retornar` un resultyado con la palabra `return`.
>[!TIP]
> como retorno tambien se puede utlizar la `funcion INTERNA`,`print()`, para depuracion de codigo no es recomnedable usarlo en produccion.
AVERIGUAR FUNCINESINTERNAS
> `PRINT` ES UNA HERRMIENTA PARA DEPURAR Y COMPARAR SI UNA FUNCION ESTA ASIENDO LA TAREA CORRECTA
**ejemplo:**
```python
def saludo():
    saludo="hola chivo"
    saludo_dos="como estas"
    return saludo+saludo_dos
saludo(saludo())
# saludo()
```

### invocar una funcion
para invocar (llamar, ejecutar una funcion solo tendremos que escribir el `nombre`de la fucniuon seguido por `()` parantesis.
```python
def saludo():
    print("hola")
#invocando la funcion
saludo()
```

## retornar una valor
las funcuiones pueden retornar o devolver un valor 
```python
def uno():
    return 1
uno()
```

> [!warning]
> no confundir `print ()` con `return`, el valor retornado por `return` nos permite usarlo fuera de su contexto, y `print()` solo mostrara el literal por terminal.
**ejemplo**
*en el archivo `lecture.py`
## retornando multiples valores
el secxretob e hacerlo mediante un ipo de dato estructurado
```python
def tupla():
    resturn 2,3,4
varios()
#retorna (2,3,4)
def lista():
    return{"hola", 45}
#retorna["hola",45]
def dicc():
    return´["nombre":"jose","edad":45]

## parametros y argumentos
si una funcion n dispusiera de valores de entrada esatraia limitada en su actuaicion .
es por ello los parametros nos permite variar los datos de consume una funcion para obtener distintos resultados
***ejemplo***
*crear una funcion que recibe un valor numerico y retorna su raiz cuadrada*
```python
def sqtr(valor):
    return valor**(1/2)
    ## nota: en este caso, el valor 4es un argumento de la funcion
sqrt(4)
```
cuando llamamos a una funcion con arguemento `argumentos`, los valores de estos arguemntos se copian en los correspondientes `parametros` dentro de la funcion.
````python
def ejm(a,b,c):
    return a+b+c
    ejm(4,5,6)
```
### argumentos dominales
es esta aproximacios los atgumentos no son copiados en un orden especifico sino que **se asignan por  nombre acada parametro**. ello nos permite evitar  problemas de conocer on recordar cual es el orden de los parametros de la defimicion de la funcion, para utlizarlo, basta con realizar una assignacion de cada asignacion de cada argumento en la propia llamada al funcion
**ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
        la cpu es dela familia(familia),
        con (num_core) cores y con una 
        frecuencia de (frecuencia)
    """)
build_cpu(num_core=4,familia="intel",frecuencias=2.7)
```
### argumentos posicionales
los argumentos son copiados es un orden especifico, es este caso debmos conocer o recordar cual es el orden de los parametros
**ejemplo**
def build_cpu(familia,num_core,frecuencia):
    print(f"""
        la cpu es dela familia(familia),
        con (num_core) cores y con una 
        frecuencia de (frecuencia)
    """)
# haciendo uso de argumentos posicionales
build_cpu("intel",4,2.7)
```
### parametros por defecto 
es posible especificar **valores por defecto** en los parametros de una funcion, en el caso de que no se proporciene un valor al argumento en la llamada a la funcion, elparametro correspondientetomara el valor definidopor valor.
**ejemplo**
```ejemplo**
```python
def alumnos(nom,app,estado="aprobado"): 

alumnos("ruth","castillo")
alumnos("anthony","cruces";"desaprobado")
```
## desempaquetados/empauquetados(tarea)

##Empaquetar/Desempaquetar argumentos
Python nos ofrece la posibilidad de empaquetar y desempaquetar argumentos cuando estamos invocando a una función, tanto para argumentos posicionales como para argumentos nominales.
Y de esto se deriva el hecho de que podamos utilizar un número variable de argumentos en una función, algo que puede ser muy interesante según el caso de uso que tengamos.
##Empaquetar/Desempaquetar argumentos posicionales
Si utilizamos el operador * delante del nombre de un parámetro posicional, estaremos indicando que los argumentos pasados a la función se empaqueten en una tupla.
```sum(4, 3, 2, 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum() takes at most 2 arguments
##Empaquetar/Desempaquetar argumentos nominales
Si utilizamos el operador ** delante del nombre de un parámetro nominal, estaremos indicando que los argumentos pasados a la función se empaqueten en un diccionario.
Supongamos un ejemplo en el que queremos encontrar la persona con mayor calificación de un examen. Haremos uso del ** para empaquetar los argumentos nominales:
def best_student(**marks):
    print(f'{marks=}')
    max_mark = -1
    for student, mark in marks.items():  # marks es un diccionario
        if mark > max_mark:
            max_mark = mark
            best_student = student
    return best_student
## funciones internas de python(tarea)

Bienevenidos sean a este post, hoy hablaremos sobre dos temas particulares de las funciones.


Atributos
Toda funcion es un objeto hecho y derecho y por lo tanto poseen atributos, algunos son especiales y pueden ser usados de manera introspectiva para inspeccionarlo durante la ejecucion, para entender el concepto vamos a analizar el siguiente ejemplo, primero crearemos un archivo al cual llamaremos atributos.py y le agregaremos el siguiente codigo:

atributos.py
def multiplicacion(a, b=1) :
	"""Devuelve a multiplicado por b."""
	return a * b

atributos_especiales = [
	"__doc__", "__name__", "__qualname__", "__module__",
	"__defaults__", "__code__", "__dict__", "__closure__", 
	"__annotations__", "__kwdefaults__",
]

for atributo in atributos_especiales :
	print(atributo, '->', getattr(multiplicacion, atributo))
A
Primero vamos a crear una funcion llamada multiplicacion, en esta funcion multiplicaremos los valores recibidos y lo devolveremos por medio de return, tenemos una linea interesante que explicaremos mas adelante y se llama documentacion por ahora diremos que nos sirve para comentar que hace esta funcion, luego crearemos una lista para almacenar la identificacion de algunos de los atributos especiales que tenemos disponibles:


__doc__, nos devuelve la documentacion
__name__, nombre de la funcion
__qualname__, idem al anterior pero provee una mejor denominacion en algunos casos
__module__, nos indica que modulo esta siendo usado
__defaults__, nos devuelve los valores predeterminados que establecimos
__code__, nos indica cual es el codigo que utilizamos
__dict__, nos devuelve los diccionarios creados
__closure__, nos informa las variables encerradas en funciones anidadas
__annotations__, nos indica las expresiones asociadas a los argumentos de las funciones
__kwdefaults__, nos indica las palabra clave predeterminadas despues argumentos posicionales variables



