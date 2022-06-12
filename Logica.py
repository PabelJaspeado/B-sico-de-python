def Cliente(Nombre):
    if Nombre == "Colocas el nombre deseado":
        return True
    else:
        print("Usuario Invalido. ")
        return 
        

def Transferencia(USD): 
    if USD >= 1000000:
        return True
    elif USD < 100000:
        print("Para realizar la operación debe ser mayor a $1,000,000. ")
        return 

def run():
    Nombre = input("¿Cúal es su nombre? ")
    if Cliente(Nombre):
        print("Cliente valido...")
        USD = int(input("¿Cúanto Dinero desea transferir? "))
        if Transferencia(USD):
            print("Transacción realizada.")


menu = """
¡Bienvenido al Sistema de su Banco Virutal!

Presione "Enter" para continuar.
"""

opción = input(menu)


if __name__ == "__main__":
    run()