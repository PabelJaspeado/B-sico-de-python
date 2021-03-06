import random


def generar_contrasegna():
    mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    simbolos = ["!","'", "#", "$", "%", "&", "/", "(", ")", "=", "?", "¡", "*", "[", "]", "_", ":", ";"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasegna = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasegna.append(caracter_random)
    
    contrasegna = "".join(contrasegna)
    return contrasegna


def run():
    contrasegna = generar_contrasegna()
    print("Tu nueva contraseña es: " + contrasegna)


if __name__ == "__main__":
    run()