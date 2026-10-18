#jugadores de baloncesto y segun altura, posicion
altura = float(input("Ingrese altura de jugador: "))

if altura < 160:
    print("Posicion: Base")
    
elif altura >= 160 and altura <= 179:
    print("Posicion: Escolta")
    
elif altura >= 180 and altura <= 199:
    print("Posicion: Alero")
    
else: 
    print("Posicion: Ala-Pivot o Pivot")
    
    
    
    
    
    
#Nota Aleatoria entre 1 y 10 inclusive
nota = int(input("Ingrese su nota: "))

if nota >= 6 and nota <=10:
    print("Promocion directa, la nota es: ", nota)
    
elif nota >=4 and nota < 6:
    print("Aprobado, la nota es: ", nota)
    
elif nota < 0 or nota > 10:
    print("Nota inválida")
    
else:
    print("Desaprobado, la nota es: ", nota)
    
    
    
    
    
#agencia de viajes match case
estacion = input("Ingrese una estación del año(verano, invierno, primavera, otoño): ")
lugar = input("Ingrese un lugar de destino: ")
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
        
        
        
        
        
        
#desafio condicional servicio de agua
met_consu = int(input("Ingrese Cantidad de metros consumidos: "))
tipo_cliente = input("Ingrese Tipo de cliente (Residencial, Comercial o Industrial): ")
COSTO_POR_METRO = 200
costo_consumo = met_consu * COSTO_POR_METRO
CARGO_FIJO = 7000
subtotal_consumo = costo_consumo + CARGO_FIJO
total = subtotal_consumo
bonificacion = 0
recargo = 0

print("subtotal:",subtotal_consumo)

#Caso residencial
if tipo_cliente == "Residencial":
    if met_consu < 30:
        bonificacion = costo_consumo * 10 / 100
        print("Bonificacion 10%:", bonificacion)
        total = subtotal_consumo - bonificacion
        print("Total:",total)
    
    elif met_consu > 80:
        recargo = costo_consumo * 15 / 100
        print("Recargo 15%:",recargo)
        total2 = subtotal_consumo + recargo
        print("Total:", total)
        
    else:
        print("No hay bonificacion ni recargo: $", total)
        
#caso comercial    
elif tipo_cliente == "Comercial":
    if met_consu > 300:
        bonificacion = costo_consumo * 12 / 100
        print("Bonificacion 12%:", bonificacion)
        total = subtotal_consumo - bonificacion
        print("Total:",total)
        
    elif met_consu > 150:
        bonificacion = costo_consumo * 8/100
        print("Bonificacion 8%:", bonificacion)
        total = subtotal_consumo - bonificacion
        print("Total:", total)
        #print("No hay bonificacion ni recargo: $", subtotal_consumo)
        
    elif met_consu < 50:
        recargo = costo_consumo * 5/100
        print("Recargo 5%: ", recargo)
        total= subtotal_consumo + recargo
        print("Total:", total)
        
    else:
        print("No hay bonificacion ni recargo", total)
        
#Caso industrial       
elif tipo_cliente == "Industrial":
    if met_consu > 1000:
        bonificacion = costo_consumo * 30 / 100
        print("Bonificacion 30%:", bonificacion)
        total = subtotal_consumo - bonificacion
        print("Total:",total)
        
    elif met_consu > 500:
        bonificacion = costo_consumo * 20 / 100
        print("Bonificacion 20%:", bonificacion)
        total = subtotal_consumo - bonificacion
        print("Total:",total)
        
    elif met_consu < 200:
        recargo = costo_consumo * 10 / 100
        print("Recargo 10%:", recargo)
        total = subtotal_consumo + recargo
        print("Total:",total)
        
    else:
        print("No hay bonificacion ni recargo", total)
        
#Caso especial recidencial
if tipo_cliente == "Residencial" and subtotal_consumo < 35000:
    descuento = subtotal_consumo * 5 / 100
    print("Descuento", descuento)
    total = total - descuento
    print("Total_con_descuento:", total)
    
# IVA para todos los clientes
IVA = 21 / 100
iva = total * IVA
total_final = total + iva

print("Tipo de Cliente: ", tipo_cliente)
print("Metros consumidos: ", met_consu)
print("Bonificacion: ", bonificacion)
print("Recargo: ", recargo)
print("Total Parcial", total)
print("IVA:", iva)
print("Total final a pagar:", total_final)