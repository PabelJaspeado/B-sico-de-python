def conversor(divisa, valor_divisa, texto_moneda):
    pesos = input("驴Cu谩ntos pesos Mexicanos tienes?: ")
    pesos = float(pesos)
    divisa = pesos / valor_divisa
    divisa = round(divisa, 2)
    divisa = str(divisa)
    print("Tienes $" + divisa + texto_moneda)

menu = """
Bienvenido al conversor de monedas 馃挼 馃挾 馃挻 馃挿

1 - Dolares.
2 - Euros.
3 - Yenes.
4 - Libras.

Elije una opci贸n: """

opci贸n = int(input(menu))

if opci贸n == 1:
    conversor("d贸lares", 20.30, " d贸lares")
elif opci贸n == 2:
    conversor("euros", 23.17, " euros")
elif opci贸n == 3:
    conversor("yenes", 2.79, " yenes")
elif opci贸n == 4:
    conversor("libras", 27.86, " libras")
else:
    print("Ingresa la opci贸n correcta, Puto.")



