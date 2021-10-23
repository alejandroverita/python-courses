DATA = [
    {
        "name": "Facundo",
        "age": 72,
        "organization": "Platzi",
        "position": "Technical Coach",
        "language": "python",
    },
    {
        "name": "Luisana",
        "age": 33,
        "organization": "Globant",
        "position": "UX Designer",
        "language": "javascript",
    },
    {
        "name": "Héctor",
        "age": 19,
        "organization": "Platzi",
        "position": "Associate",
        "language": "ruby",
    },
    {
        "name": "Gabriel",
        "age": 20,
        "organization": "Platzi",
        "position": "Associate",
        "language": "javascript",
    },
    {
        "name": "Isabella",
        "age": 30,
        "organization": "Platzi",
        "position": "QA Manager",
        "language": "java",
    },
    {
        "name": "Karo",
        "age": 23,
        "organization": "Everis",
        "position": "Backend Developer",
        "language": "python",
    },
    {
        "name": "Ariel",
        "age": 32,
        "organization": "Rappi",
        "position": "Support",
        "language": "",
    },
    {
        "name": "Juan",
        "age": 17,
        "organization": "",
        "position": "Student",
        "language": "go",
    },
    {
        "name": "Pablo",
        "age": 32,
        "organization": "Master",
        "position": "Human Resources Manager",
        "language": "python",
    },
    {
        "name": "Lorena",
        "age": 56,
        "organization": "Python Organization",
        "position": "Language Maker",
        "language": "python",
    },
]


def run():
    # -------------------------- LIST COMPREHENSIONS
    all_python_devs = [
        worker["name"] for worker in DATA if worker["language"] == "python"
    ]

    print(all_python_devs)

    all_platzi_workers = [
        worker["name"] for worker in DATA if worker["organization"] == "platzi"
    ]
    print(all_platzi_workers)

    adults = [worker["name"] for worker in DATA if worker["age"] >= 18]
    print(adults)

    # z = x | y Para el diccionario worker en DATA, voy a guardar en ese mismo diccionario una nueva key llamada old que regrese un True si la key age es mayor a 60, y que regrese un False si es menor a 60.
    old_people = [worker | {"old": worker["age"] > 60} for worker in DATA]
    print(old_people)

    # ------------------------- LAMBDA FUNCTIONS

    # FILTER receives two parameters: lambda function and an iterable object
    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))
    print(all_python_devs)

    all_platzi_workers = list(
        filter(lambda worker: worker["organization"] == "Platzi", DATA)
    )
    all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers))
    print(all_platzi_workers)

    adults = list(filter(lambda worker: worker["age"] >= 18, DATA))
    # overwritting variable adults to get just the people's name older than 18
    adults = list(map(lambda worker: worker["name"], adults))
    print(adults)

    # Join a dictionary with '|'. Add a new parameter to the object, this time, people older than 60
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 60}, DATA))
    print(old_people)


if __name__ == "__main__":
    run()
