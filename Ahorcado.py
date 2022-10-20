import random


def read():
    list = []
    with open("./Data.txt", "r", encoding="UTF-8") as f:
        for palabras in f:
            list.append(palabras)
    palabra = random.choices(list)
    palabra = "".join(palabra)
    print(palabra)


'''def consultar_letra():
    pass


def animaciones():
    pass


def menu():
    pass


def palabra():
    pass'''


def vidas():
    pass


def run():
    read()


if __name__ == "__main__":
    run()