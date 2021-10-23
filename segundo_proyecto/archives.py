def read():
    names = []
    with open("./archives/name.txt", "r", encoding="utf-8") as f:
        for line in f:
            # strip() is used to delete spaces in the line
            if len(line.strip()) > 0:
                names.append(line.strip())
            if len(names) > 0:
                print(names)

            else:
                print("Archivo vacio")


def write(texto):
    names = [texto]
    with open("./archives/new.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def add_name(name):
    with open("./archives/name.txt", "a", encoding="utf-8") as f:
        f.write(name)
        f.write("\n")


def delete_name(name):
    pass


def run():
    start_program = True
    while start_program:
        try:
            print(
                """ 
            ----------------------------------------------------------------------
                Seleccione un numero:
                1. Crear un nuevo archivo 
                2. Agregar nombre
                3. Listar nombre
                4. Salir del programa
            ----------------------------------------------------------------------
            """
            )

            n = int(input("Ingrese un valor: "))

            if n == 1:
                texto = input("Ingresa un texto: ")
                write(texto)

            elif n == 2:
                name = input("Ingrese un nombre: ")
                add_name(name)

            elif n == 3:
                read()

            elif n == 4:
                start_program = False
                print("Gracias por usar el programa")

        except ValueError:
            print("Error, seleccione una opcion valida")


if __name__ == "__main__":
    run()
