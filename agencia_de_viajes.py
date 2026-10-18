estacion_año = input("Ingrese una estacion del año: ")

if estacion_año == "invierno":
    print("solo se viaja a Bariloche.")
    
elif estacion_año == "verano":
    print(" se viaja a Mar del plata y Cataratas.")
    
elif estacion_año == "otoño":
    print("se viaja a todos los lugares.")

elif estacion_año == "primavera":
    print("se viaja a todos los lugares menos Bariloche.")
    
else:
    print("No se viaja")
    
#otra forma que encontre:
estacion_año = input("Ingrese una estación del año: ")
lugar = input("Ingrese un lugar: ")

if estacion_año == "invierno" and lugar == "Bariloche":
    print("Se viaja")
    
elif estacion_año == "verano" and (lugar == "Mar del plata" or lugar == "Cataratas"):
    print("Se viaja")
    
elif estacion_año == "otoño":
    print("Se viaja")
    
elif estacion_año == "primavera" and lugar != "Bariloche" :
    print("Se viaja")
    
else:
    print("No se Viaja")
    
    
#Forma con match
#Match

estacion = input("Ingrese una estación: ")
lugar = input("Ingrese un lugar: ")
match estacion:
    case "invierno":
        if lugar == "Bariloche":
            print("Se viaja")
        else:
            print("No se viaja")
    case "verano":
        if lugar == "Mar del Plata" or lugar == "Cataratas":
            print("Se viaja")
        else:
            print("No se viaja")
    case "otoño":
        print("Se viaja")
    case "primavera":
        if lugar != "Bariloche":
            print("Se viaja")
        else:
            print("No se viaja")
    case _:
        print("Estación inválida")
