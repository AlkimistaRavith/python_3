import getpass
from string import ascii_lowercase

#En github no se registran simbolos por letras ingresadas en password.
password = getpass.getpass("Ingrese una contraseña: ")
password = password.lower()
password = password.replace(" ", "$")

intentos = 0
activar = 0

#Condicional para restringir uso a solo letras
for letra in password:
    if letra not in ascii_lowercase:
        print("La contraseña solo debe contener letras del abecedario (sin ñ, números, símbolos ni espacios). \nPor favor inténtalo nuevamente.")
        activar = "no"
        break
    else:
        activar = "si"

if activar == "si" :
    #función para registrar la cantidad de intentos por iteración
    def contar_intentos(password):
        #para que no importe si se escribe con mayuscula o minuscula.
        password = password.lower()
        intentos = 0

        #iteración de cada letra.
        for letra in password:
            #comapración y contador de intentos.
            for letra_abecedario in ascii_lowercase:
                intentos += 1
                if letra == letra_abecedario:
                    break 
        #regreso a intentos = 0 para volver a contar.
        return intentos

    #suma de los contar_intentos por cada iteración.
    total_intentos = contar_intentos(password)

    print(f"La contraseña fue forzada en {total_intentos} intentos.")