def palindromo(frase):
    frase_invertida = frase[::-1]
    if frase_invertida == frase:
        return True
    else:
        return False


def run():
    frase = input("Escribe una frase: ")
    frase = frase.lower()
    frase = (
        frase.replace(" ", "")
        .replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
    )
    es_palindromo = palindromo(frase)
    if es_palindromo == True:
        print("Es un palindromo! :D")
    else:
        print("No es un palindromo :c")


if __name__ == "__main__":
    run()
