import time


class FiboIter:
    def __init__(self, nmax):
        self.nmax = nmax

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter = +1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2

            if self.counter == self.nmax:
                print("Finished")
                raise StopIteration

            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux


def run():
    try:
        nmax = int(input("Escribe la cantidad de ciclos en el Fibonacci: "))

        if nmax > 0:
            fibonacci = FiboIter(nmax)

            for element in fibonacci:
                print(f"{element}")
                time.sleep(1)

        elif nmax == 0:
            print(0)

        else:
            raise ValueError

    except ValueError:
        print("Ingresa un numero positivo")
        run()


if __name__ == "__main__":
    run()
