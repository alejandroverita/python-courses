def prime_numbers(num: int) -> bool:
    counter: int = 0
    if num == 1:
        return False
    for i in range(1, num + 1):
        if i == 1 or i == num:
            continue
        if num % i == 0:
            counter += 1

    if counter == 0:
        return True
    else:
        return False


def is_palindrome(word: str) -> bool:
    # The strip() method removes any spaces at the beginning and at the end
    word = word.replace(" ", "").lower()
    print(word)
    # it returns the word from back to front
    return word == word[::-1]


def run():
    number: int = int(input("Ingresa un numero: "))
    is_prime: bool = prime_numbers(number)
    if is_prime == True:
        print(f"The number {number} is a prime number")
    else:
        print(f"The number {number} is not a prime")


if __name__ == "__main__":
    run()
