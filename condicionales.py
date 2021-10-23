numero = int(input("Ingresa tu edad: "))

if numero >= 18 and numero < 80:
    print("Puedes pasar")
elif numero >= 80 and numero < 120:
    numero = str(numero)
    print("Tu edad es: " + numero + ". " + "Debes cuidar tu salud")
elif numero < 18 and numero > 0:
    print("Estas muy joven, chaval")
else:
    print(
        """
    ***********************
    Error
    ***********************
    Ingresa un numero validoo"""
    )
