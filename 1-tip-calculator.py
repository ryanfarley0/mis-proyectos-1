def encontrar_la_propina(porcentaje,total):
    propina=total*(porcentaje/100)
    return propina
while True:
    try:
        total= float(input("Ingrese el monto total: "))
        porcentaje= float(input("Ingrese el porcentaje de propina que desea acreditar: "))
        propina=encontrar_la_propina(porcentaje,total)
        total_con_propina= propina + total
        print("El total con propina es :",total_con_propina,"$")
        break
    except ValueError: 
        print("Por favor, ingrese valores validos.")

