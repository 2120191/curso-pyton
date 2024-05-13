
# vocales
vocales:str="aeiou"
print(vocales[0])
print(vocales[1])
print(vocales[2])
print(vocales[3])
print(vocales[4])

vocales:str="aeiou"
for n in range(0,5):
    print(vocales[n])

for n in range(1,17):
    if n%2==0:
        print(n)

for n in range(1,17):
    if n%2==0:
        print(f"(n) es el par numero (contador)")        

oracion:str=input("escribe una oracion: ")
contador:int=0
for n in range(0,len(oracion)):
    if oracion[n]=="a":
        contador=contador+1
        #contador+=1
for n in "aeiou":
    print(n)
print(f"la cantidad de letras  que tengo es (contador)")    

for i,l in enumerate("aeiou"):
    print(f"el indice es (i) y la letra es (l)")
print(f"la cantidad de letras  que tengo es (contador)")    

oracion:str=inpu("escribe una oracion: ")
contador:int=0
for n in range (0,len(oracion)):
    if oracion[n]==",":
        contador=contador+1
for n in ",":
    print(,)
print(f"la cantidad de letras que tengo es(contador)")    