PESOS_CHILENOS = 700
PESOS_COLOMBIANOS = 3959
PESOS_ARGENTINOS = 99
PESOS_MEXICANOS = 20


def exchanges(moneda, cantidad):
    result = 0
    # Moneda chilena
    if moneda == 1:
        result = cantidad / PESOS_CHILENOS
        result = round(result, 2)
        print(f"Los {cantidad} pesos chilenos equivalen a {result} dolares")
    # Moneda colombiana
    elif moneda == 2:
        result = cantidad / PESOS_COLOMBIANOS
        result = round(result, 2)
        print(f"Los {cantidad} pesos colombianos equivalen a {result} dolares")
    # Moneda Argentina
    elif moneda == 3:
        result = cantidad / PESOS_ARGENTINOS
        result = round(result, 2)
        print(f"Los {cantidad} pesos argentinos equivalen a {result} dolares")
    # Moneda mexicana
    elif moneda == 4:
        result = cantidad / PESOS_MEXICANOS
        result = round(result, 2)
        print(f"Los {cantidad} pesos mexicanos equivalen a {result} dolares")
    # Otro
    else:
        print("Ingresa solo un numero de la lista")


if __name__ == "__main__":
    try:
        moneda = int(
            input(
                """
            Ingresa el indice de la moneda que quieres convertira  dolar:
                [1] Moneda chilena a Dolar
                [2] Moneda colombiana a Dolar
                [3] Moneda argentina a Dolar
                [4] Moneda mexicana a Dolar
            Selecciona: """
            )
        )

        print("********************************")
        cantidad = int(input("Ingresa la cantidad que quieres convertir: "))
        exchanges(moneda, cantidad)

    except:
        print("* * * * * * E R R O R * * * * * *")
        print("Por favor, Ingresa solo valores numericos")
