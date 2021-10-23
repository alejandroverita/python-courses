import time


def fibo_gen(max_number):
    n1 = 0
    n2 = 1
    counter = 0
    aux = 0

    while aux < max_number:

        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux


if __name__ == "__main__":
    max_number = int(input("Escribe un numero maximo de la secuencia Fibonacci: "))

    fibo = fibo_gen(max_number)

    last_number = 0
    for element in fibo:
        if element < max_number:
            print(element)
            time.sleep(0.5)
            last_number = element

    print(f"El numero maximo de {max_number} en el ciclo Fibonacci es: {last_number}")
