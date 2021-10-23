def run():
    my_dict = {i: round(i ** 0.5, 2) for i in range(1, 101)}
    print(my_dict)

    # for i in range(1, 11):
    #     if i % 3 != 0:
    #         my_dict[i] = i ** 3
    #         print(f"{i} al cubo es igual {my_dict[i]}")


if __name__ == "__main__":
    run()
