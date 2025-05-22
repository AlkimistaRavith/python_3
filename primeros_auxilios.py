import time

emergencia = 0
#estimulos
paso1 = 0
#respira
paso2 = 0
#signos de vida
paso3 = 0
#ambulancia
paso4 = 0
paso5 = 0

print("Has ingresado a la asistencia de emergencias médicas.")

while emergencia == 0 :
    inicio = input("Confirma si estás frente a una emergencia médica (Si/No): ")
    inicio = inicio.lower()

    if inicio == "si" or inicio == "s" :
        emergencia = "activo"
        paso1 = "activo"
    elif inicio == "no" or inicio == "n" :
        emergencia = "fin"
    else :
        print("La opción ingresada no es válida. (1)")
        emergencia = 0

while emergencia == "activo" :
    #activación paso 1
    if paso1 == "activo" :
        paso1 = input("¿La persona responde a estímulos? (si/no): ")
        #condicional paso 1    
        if paso1 == "si" or paso1 == "s" :
            print("Llevala al hospital más cercano.")
            paso1 = 0
            emergencia = "fin"
        elif paso1 == "no" or paso1 == "n" :
            print("Despeja las vías aéreas (boca y nariz)")
            paso1 = 0
            paso2 = "activo"
        else :
            print("Respuesta no válida, por favor responde de nuevo. (2)")
            paso1 = "activo"

    #activación paso 2
    if paso2 == "activo" :
        paso2 = input("¿La persona está respirando? (si/no): ")
        #condicional paso 2
        if paso2 == "si" or paso2 == "s" :
            print("Deja que la habitación tenga ventilación, y recuesta a la persona, para permitirle respirar mejor")
            paso2 = 0
            emergencia = "fin"
        elif paso2 == "no" or paso2 == "n" :
            print("Administra 5 ventilaciones y llama a una Ambulancia.")
            paso2 = 0
            paso3 = "activo"
            paso4 = "activo"
        else :
            print("Respuesta no válida, por favor responde de nuevo. (3)")
            paso2 = "activo"

    #activación paso 3 y paso 4
    while paso4 == "activo" :
        #paso 3
        if paso3 == "activo" :
            paso3 = input("¿La persona tiene signos de vida activos? (si/no): ")
            #condicional paso 3
            if paso3 == "si" or paso3 == "s" :
                print("Manten bajo vigilancia sus signos vitales por 5 minutos, hasta que llegue la Ambulancia")
                paso3 = "fin"
                paso4 = "activo"
                paso5 = "activo"
                time.sleep(0.5)
                print("Tiempo de espera = 5 minutos...")
                #Solo se aplica 10 segundos para probar, podría ajustarse a 2 minutos o 5 minutos para volver a consultar.
                time.sleep(10)
            elif paso3 == "no" or paso3 == "n" :
                print("Administra Compresiones torácicas hasta que recupere su signos vitales o llegue la Ambulancia.")
                time.sleep(0.5)
                print("Tiempo de espera = 5 minutos...")
                #Solo se aplica 10 segundos para probar, podría ajustarse a 2 minutos o 5 minutos para volver a consultar.
                time.sleep(10)
                paso3 = "fin"
                paso4 = "activo"
                paso5 = "activo"
            else :
                print("Respuesta no válida, por favor responde de nuevo. (4)")
                paso3 = "activo"
                paso4 = "activo"
        #paso5
        if paso5 == "activo" :
            paso5 = input("Llegó la ambulancia? (si/no): ")
            #paso5: llegada de ambulancia
            if paso5 == "si" or paso5 == "s" :
                print("Informa detalladamente lo ocurrido al paramédico. Y permite que continue con la atención de la emergencia.")
                paso3 = "fin"
                paso4 = "fin"
                paso5 ="fin"
                emergencia = "fin"
            elif paso5 == "no" or paso5 == "n" :
                paso3 = "activo"
                paso4 = "activo"
                paso5 = "activo"
            else :
                print("Respuesta no válida, por favor responde de nuevo. (5)")
                paso5 = "activo"
                paso3 = "fin"
                paso4 = "activo"       

print("Esperamos hay sido de utilidad esta herramienta. \n Adiós!")