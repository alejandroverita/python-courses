import random


def run():
    contador = 0
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Escribe un numero entre 1 y 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("\nTu numero es menor. Elige otro mas alto ")

        else:
            print("\nTu numero es muy grande. Elige otro mas bajo")
        numero_elegido = int(input("Elige otro numero: "))
        contador += 1
    print("\n********")
    print("GANASTE!")
    print(f"Intentaste {contador} veces")


if __name__ == "__main__":
    run()
