menu = input(
    """ 
    **********************
    BIENVENIDOS
    Elige un producto
    1. Computadora
    2. Celular
    3. Television

    Ingresa un numero: """
)

menu = int(menu)


def conversacion(opcion, valor):
    valor = str(valor)
    print("Hola")
    print("El precio de tu " + opcion + " es " + valor)
    print("Un gusto. Vuelva de nuevo")
    print(
        """
        **************************
        FIN DEL PROGRAMA
    """
    )


if menu == 1:

    conversacion("computadora", 500)
elif menu == 2:

    conversacion("celular", 450)
elif menu == 3:

    conversacion("Television", 650)
else:
    print("Ingresa un numero valido")
