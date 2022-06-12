def conversor(divisa, valor_divisa, texto_moneda):
    pesos = input("¿Cuántos pesos Mexicanos tienes?: ")
    pesos = float(pesos)
    divisa = pesos / valor_divisa
    divisa = round(divisa, 2)
    divisa = str(divisa)
    print("Tienes $" + divisa + texto_moneda)

menu = """
Bienvenido al conversor de monedas 💵 💶 💴 💷

1 - Dolares.
2 - Euros.
3 - Yenes.
4 - Libras.

Elije una opción: """

opción = int(input(menu))

if opción == 1:
    conversor("dólares", 20.30, " dólares")
elif opción == 2:
    conversor("euros", 23.17, " euros")
elif opción == 3:
    conversor("yenes", 2.79, " yenes")
elif opción == 4:
    conversor("libras", 27.86, " libras")
else:
    print("Ingresa la opción correcta, Puto.")



