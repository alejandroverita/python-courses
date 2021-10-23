# [1,1,1,3,3,4,5,] -> [1,3,4,5]


def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def remove_with_sets(some_list):
    # Set items are unordered, unchangeable, and do not allow duplicate values.
    return set(some_list)


def run():
    random_list = [1, 1, 3, 5, 5, 2, 2, 4]
    print(remove_with_sets(random_list))


if __name__ == "__main__":
    run()
