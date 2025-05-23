import getpass
from string import ascii_lowercase

password = getpass.getpass("Ingrese una contraseña: ")
password = password.lower()
intentos = 0

def contar_intentos(password):
    password = password.lower()
    intentos = 0

    for letra in password:
        for letra_abecedario in ascii_lowercase:
            intentos += 1
            if letra == letra_abecedario:
                break  # Se adivinó la letra, pasar a la siguiente

    return intentos