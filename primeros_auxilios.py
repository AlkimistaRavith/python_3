emergencia = 0
paso1 = 0
paso2 = 0
paso3 = 0
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
        print("La opción ingresada no es válida")
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
        print("Respuesta no válida, por favor responde de nuevo.")
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
    else :
        print("Respuesta no válida, por favor responde de nuevo.")
        paso2 = "activo"

    #activación paso 3
    while paso3 == "activo" :
        if paso3 == "activo" :
            paso3 = input("¿La persona tiene signos de vida activos? (si/no): ")
        #condicional paso 3
        if paso3 == "si" or paso3 == "s" :
            print("Manten bajo vigilancia sus signos vitales, hasta que llegue la Ambulancia")
            paso3 = "activo"
            paso4 = "activo"
        elif paso3 == "no" or paso3 == "n" :
            print("Administra Compresiones torácicas hasta que recupere su signos vitales o llegue la Ambulancia.")
            paso3 = "activo"
            paso4 = "activo"
            paso5 = "activo"
            emergencia = "fin"
        else :
            print("Respuesta no válida, por favor responde de nuevo.")
            paso3 = "activo"
        
        if paso4 == "activo" :
            


        emergencia = "fin"
            


print("Adiós")