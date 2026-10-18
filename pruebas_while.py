#Integrador while
#Realizar un programa que permita que el usuario ingrese todos los números que desee.
contador_neg = 0
contador_positivo = 0
suma_neg = 0
suma_positivo = 0
continuar = "si"
mayor_positivo = 0
encontre_positivo = True
while continuar == "si":
    numero = int(input("Ingrese un Numero: "))
    print("Numero Ingresado: ", numero)
    
    if numero >= 0:
        contador_positivo = contador_positivo +1
        suma_positivo = suma_positivo + numero
        
        
        if encontre_positivo == True:
            mayor_positivo = numero
            encontre_positivo = False
            
        else:
            if numero > mayor_positivo:
                mayor_positivo = numero
        
    elif numero == 0:
        print("El numero es cero:", numero)
        
    else:
        contador_neg = contador_neg +1
        suma_neg = suma_neg + numero
        
        
    continuar = input("Quiere continuar? (si/no): ")
    
if contador_positivo >= 1:
    prom_num_positivos = suma_positivo / contador_positivo
    
    
total_ingresos = contador_neg + contador_positivo

porcentaje_negativos = (contador_neg * 100) / total_ingresos

print("Cantidad de Negativos: ", contador_neg)
print("Cantidad de Positivos", contador_positivo)
print("Suma total positivos: ", suma_positivo)
print("Suma total negativos: ", suma_neg)
print("El promedio de los numeros positivos es: ", prom_num_positivos)
print("El numero positivo mas alto es: ", mayor_positivo)
print("Porcentaje de números negativos:", porcentaje_negativos, "%")









#while validaciones.
#Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.
#clave = input("Ingrese la clave: ")
#while clave != "nico":
    #print("La clave es incorrecta: ", clave)
    #clave = input("Ingresar otra clave: ")

#print("Clave correcta", clave)
    
#Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos. 
clave = input("Ingrese la clave: ")
intentos = 1
while clave != "nico" and intentos < 3:
    print("La clave es incorrecta: ", clave)
    print("Intentos permitidos: 3")
    clave = input("Ingresar otra clave: ")
    intentos += 1 
    
if intentos == 3:
    print("No hay mas intentos: ", intentos)
else: 
    print("Clave correcta:", clave)