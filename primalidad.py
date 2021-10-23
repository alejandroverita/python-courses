def es_primo(numero):
    contador = 0
    if numero == 1:
        return False
    else:
        contador = 0
    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        elif numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    numero = int(input("Ingresa un numero: "))
    if es_primo(numero):
        print(f"El {numero} es un numero primo")
    else:
        print(f"El {numero} no es un numero primo")


if __name__ == "__main__":
    run()
