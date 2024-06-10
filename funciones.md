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