import random


def password_generator():
    MAYUS = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "Ñ",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "X",
        "Y",
        "Z",
    ]
    MINUS = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "ñ",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "x",
        "y",
        "z",
    ]
    NUMS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    CHARS = [
        "*",
        "+",
        "-",
        "/",
        "@",
        "_",
        "?",
        "!",
        "[",
        "{",
        "(",
        ")",
        "}",
        "]",
        ",",
        ";",
        ".",
        ">",
        "<",
        "~",
        "°",
        "^",
        "&",
        "$",
        "#",
        '"',
    ]

    character = MAYUS + MINUS + NUMS + CHARS

    # Save random characters of the list above
    password = []

    for i in range(15):

        # Choise is a special function of random module. It chooses a random character and save it
        random_character = random.choice(character)

        # Adding that one random character and push into the variable
        password.append(random_character)

    # the list in a string because it can only concatenate str not 'list'
    password = "".join(password)

    # it saves on the variable password in the run() function
    return password


def run():
    password = password_generator()
    print("Tu contrasenia es: " + password)


if __name__ == "__main__":
    run()
