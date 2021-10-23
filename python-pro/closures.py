def multiplier(name: str) -> str:
    # Tener una nested function
    def mult_name(quantity: int) -> str:

        # assertstatement <condicion>, <"mensaje">
        assert type(name) == str, "Solo puedes ingresar texto"

        # referenciar un valor de un scope superior
        return name * quantity

    # La función que envuelve la nested debe retornarse
    return mult_name


def run():
    name_to_mult = multiplier("Alejandro")
    print(f" {name_to_mult(4)} ")


if __name__ == "__main__":
    run()
