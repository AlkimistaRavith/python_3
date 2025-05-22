
paso1 = 0

inicio = input("Has ingresado a la asistencia de emergencias médicas. \nConfirma si estás frente a una emergencia médica (Si/No): ")
inicio = inicio.lower()

if inicio == "si" or inicio == "s" :
    while paso1 != "si" or paso1 != "no" :
        paso1 = input("¿La persona respodne a estímulos?: ")
    