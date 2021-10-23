import random
from random import randint
import os


AHORCADO = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========""",
]


def load_words(level: int):
    """Load db with words and saves them as a word list acording choosen level."""

    with open("./archives/data.txt", "r", encoding="utf-8") as f:
        if level == 1:
            words = [word for word in f if len(word) <= 5]
            return words
        elif level == 2:
            words = [word for word in f if len(word) > 5]
            return words


def menu():
    """Display a menu user to choose level or exit the game."""

    print(
        """
        BIENVENIDO A
        ╭╮╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮
        ┃┃╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
        ┃╰━╯┣━━┳━╮╭━━┳━━┳━╯┃╭╮╭┳━━┳━╮
        ┃╭━╮┃╭╮┃╭╮┫╭╮┃┃━┫╭╮┃┃╰╯┃╭╮┃╭╮╮
        ┃┃╱┃┃╭╮┃┃┃┃╰╯┃┃━┫╰╯┃┃┃┃┃╭╮┃┃┃┃
        ╰╯╱╰┻╯╰┻╯╰┻━╮┣━━┻━━╯╰┻┻┻╯╰┻╯╰╯
        ╱╱╱╱╱╱╱╱╱╱╭━╯┃
        ╱╱╱╱╱╱╱╱╱╱╰━━╯ \n"""
    )

    option = None
    while option == None:
        print("Seleccione una opción: \n")
        print("1. Jugar a nivel 1 (palabras cortas). \n")
        print("2. Jugar a nivel 2 (palabras largas). \n")
        print("3. Salir.\n")
        option = input("Escriba el número de la opción: ")
        if option == "1":
            print("Ha elegido el nivel 1 (palabras cortas).")
            words = load_words(1)
            return words
        elif option == "2":
            print("Ha elegido el nivel 2 (palabras largas).")
            words = load_words(2)
            return words
        elif option == "3":
            print("Hasta una próxima.\n")
            exit()
        else:
            os.system("cls")
            print("=====================================================")
            print("|Ha ingresado una opción no válida, intente de nuevo|.")
            print("=====================================================")
            option = None
            continue


def normalize(s):
    replacements = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))

    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def random_word(word_list):
    lenght_list = len(word_list)
    # The randint() method returns an integer number selected element from the specified range.
    # The strip() method removes any spaces at the beginning and  at the end
    word = word_list[randint(0, lenght_list)].strip()
    word = normalize(word).upper()

    words = []
    with open("./archives/data.txt", "r", encoding="utf-8") as f:
        # The split() method splits a string into a list.
        words = f.read().split()

        # The choice() method returns a randomly selected element from the specified sequence.
        choice_word = random.choice(words)
        choice_word = normalize(choice_word).upper()

    return word


def play_hangman(word):
    os.system("cls")

    # Retorna la palabra random
    chosen_word = word
    print(chosen_word)

    # convert string to list
    letters = list("_" * len(chosen_word))

    written_letters = []

    # El doble de intentos que de palabras
    intents = len(chosen_word) * 2

    while letters != list(chosen_word):

        print(f"You have: {intents} intents to guess the word")

        # it prints the spaces of the letter
        print(str(letters) + "\n")

        try:
            letter = input("Write a letter: ").upper()
            if len(letter) > 1:
                raise ValueError("Just can input ONE letter")
            if letter in written_letters:
                raise ValueError("You already used that letter")
        except ValueError as ve:
            print("Error: ", ve)

        # Si no arroja errores el try, evalua el else
        else:
            os.system("cls")

            index = 0
            # add the letter to the array
            written_letters.append(letter)

            # evalua la letra con la palabra escogida
            for l in chosen_word:

                # Si esa letra es igual a la letra escogida por el usuario
                if l == letter:

                    # The pop() method removes the item at the given index from the list and returns the removed item.
                    # It removes the index '-' in order to add the letter
                    letters.pop(index)

                    # The insert() method inserts an element to the list at the specified index. Dos parametros: indice y elemento
                    letters.insert(index, letter)

                    # intents += 1
                    # print(intents)

                index += 1

            intents -= 1

            if intents <= 0:
                result = "Perdiste."
                break

            result = "Ganaste!"

    print(result, "La palabra era:", chosen_word)


def run():
    option = None
    while option != 3:
        words = menu()
        word = random_word(words)
        play_hangman(word)

    # read_word = random_word()


if __name__ == "__main__":
    run()
