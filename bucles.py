def run(veces, numero):
    if veces <= numero:

        print(f"La potencia de {veces} es {veces**2}")
        run(veces + 1, numero)
    else:
        print("Fin del programa")


if __name__ == "__main__":
    numero = int(input("Cuantas veces quieres repetir la potenciacion?: "))
    veces = 0
    run(veces, numero)
