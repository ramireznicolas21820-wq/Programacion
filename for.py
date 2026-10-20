#Mostrar los números ascendentes desde el 1 al 10
for x in range(1,11):
    print("Numeros del 1 al 10:", x)
    
#Mostrar los números descendentes desde el 10 al 1
for x in range(10,0, -1):
    print("Numeros descendentes del 10 al 1: ", x)
    
#Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
numero = int(input("Ingrese un numero: "))
print("Numeros desde 0 hasta", numero)

for x in range (0, numero + 1):
    print("La secuencia es: ", x)
    
#Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:
numero = int(input("Ingrese un número: "))
print("Tabla de multiplicar de", numero)

for x in range (1, 11):
    print("Los numeros son:", x * numero)
    
#5.Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.
contador = 0
suma = 0
for x in range(1, 11):
    numero = int(input("Ingresa un maximo de 10 numeros: "))
    print("si no quiere agregar mas numeros, ingrese 0: ")
    if numero != 0:
        print("El numeros es: ", numero)
        suma = suma + numero
        contador = contador +1
        
    else:
        print("no se agregan mas numeros")
        
#Imprimir los números múltiplos de 3 entre el 1 y el 10.
multiplos = []
for x in range(1,11):
    if x % 3 == 0:
        print("Es multiplo: ", x)
        multiplos = multiplos + [x]
        
    else:
        print("no es multiplo: ", x)
        
print(multiplos)


#Mostrar los números pares que hay desde la unidad hasta el número 50.
pares = []
for x in range(1,51):
    if x % 2 == 0:
        print("Es Par: ", x)
        pares = pares + [x]
        
    else:
        print("no pares: ", x)
       
print("Lista de pares: ", pares)






#Realizar un programa que permita mostrar una pirámide de números.
numero = int(input("Ingrese un número: "))

for fila in range(1, numero + 1):
    for columna in range(1, fila + 1):
        #range(inicio, final)incluye el inicio, pero no incluye el final.
        #por eso siempre aparece el 1 y un numero menos al fila + 1.
        print(columna, end="")
        #end="" le dice a Python que no salte de línea después de imprimir cada número
    print()
    
    
#Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. 
# Mostrar la cantidad de divisores encontrados.
numero = int(input("Ingrese un número: "))
divisores = []
cant_divi = 0
for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        cant_divi +=1
        
        
        divisores = divisores + [divisor]
        
        
print("cantidad de divisores: ", cant_divi)
print("lista de divisores: ", divisores)


#Ingresar un número. Determinar si el número es primo o no.

numero = int(input("Ingrese un número: "))

es_primo = True

for divisor in range(2, numero):
    if numero % divisor == 0:
        es_primo = False

if es_primo and numero > 1:
    print("El número es primo")
else:
    print("El número no es primo")
    
    

#Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número
#ingresado. Informar cuántos números primos se encontraron.
numero = int(input("Ingrese un número: "))
primos = []
cant_primos = 0

for candidato in range(2, numero + 1):
    es_primo = True

    for divisor in range(2, candidato):
        if candidato % divisor == 0:
            es_primo = False

    if es_primo:
        primos = primos + [candidato]
        cant_primos +=1

print(primos)    
