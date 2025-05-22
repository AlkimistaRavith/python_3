try:
    import sys

    ventas = {
        "Enero" : 15000 ,
        "Febrero" : 22000 ,
        "Marzo" : 12000 ,
        "Abril" : 17000 ,
        "Mayo" : 81000 ,
        "Junio" : 13000 ,
        "Julio" : 21000 ,
        "Agosto" : 41200 ,
        "Septiembre" : 25000 ,
        "Octubre" : 21500 ,
        "Noviembre" : 91000 ,
        "Diciembre" : 21000 ,
    }

    mayor_a = {}

    #Este bloque es para determinar si se ingresa un argumento al ejecutar el programa, o si pide opción si no se ingresó argumento.
    if len(sys.argv) == 2 :
        x = int(sys.argv[1])
    elif len(sys.argv) == 1 : 
        x = int(input("Mostrar meses con ventas mayores a: "))
    else :
        print("Esta opción no es válida. \n Puedes escribir <python mayor_a.py>, o \n <python mayor_a.py [Valor de Ventas mayor a]>")
        x = "invalido"

    #condicional para ingreso con demasiados argumentos:
    if x != "invalido" :
        #Filtro de valores de ventas.
        for clave, valor in ventas.items():
            if valor >= x:
                mayor_a[clave] = valor

        #Condicional de rango (indicar comportamiento del filtrado)
        if x > max(ventas.values()) :
            print("Ningun mes alcanzó el valor de ventas indicado.")
        elif x < min(ventas.values()) :
            print("Todos los meses superan el valor de ventas indicados:")
        else :
            print(f"Los meses con ventas mayor a {x} son:")

        #Imprime el diccionario filtrado
        print(mayor_a)

except ValueError:
    print("Has ingresado datos que no son numéricos. \n Puedes escribir <python mayor_a.py>, o \n <python mayor_a.py [Valor de Ventas mayor a]>")