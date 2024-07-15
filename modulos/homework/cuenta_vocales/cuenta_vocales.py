def cuenta_vocales(text:str):
    """funcion para contar la cantidad de vocales auq aparecen en un texto"""
    text_minusculas:str=text.lower()
    cantidad_vocales=0
    for n in text_minusculas:
        if n =="a":
            cantidad_vocales+=1
        return cantidad_vocales

mayor_edad(20)
print(es_menor([4,8,10,2,3]))
print(cuenta_vocales("mi mama me mima yo amo ami mama"))