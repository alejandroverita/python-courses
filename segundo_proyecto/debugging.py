def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def run():
    try:
        num = int(input("Ingresa un numero: "))
        if num <= 0:
            print("Numeros menores de 0 no son validos")
            raise ValueError
        print(divisor(num))
        print("Fin del programa")
    except ValueError as ve:
        print(ve)
        run()


if __name__ == "__main__":
    run()
