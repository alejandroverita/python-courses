def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def run():
    num = input("Ingresa un numero: ")
    assert num.isnumeric(), "Debes ingresar un numero positivo."

    num = int(num)
    print(divisor(num))
    print("Fin del programa")


if __name__ == "__main__":
    run()
