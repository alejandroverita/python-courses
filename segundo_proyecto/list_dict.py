def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Alejandro", "lastname": "Vera"}

    super_list = [
        {"firstname": "Jessica", "lastname": "Gonzalez"},
        {"firstname": "Miguel", "lastname": "Martinez"},
        {"firstname": "Josue", "lastname": "Palma"},
        {"firstname": "Jimmy", "lastname": "Gorozabel"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.1, 2.4, 3, 2, 4.1],
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    print("*" * 5)

    for i in super_list:
        print(f'{i["firstname"]}: {i["lastname"]}')


if __name__ == "__main__":
    run()
