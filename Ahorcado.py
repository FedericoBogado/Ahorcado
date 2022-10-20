import random


def read():
    list_pal = []
    a,b = 'áéíóúüñ','aeiouun'
    with open("./Data.txt", "r", encoding="UTF-8") as f:
        for palabras in f:
            list_pal.append(palabras)
    palabra_ram = random.choices(list_pal)
    palabra_ram = "".join(palabra_ram)
    palabra_ram = palabra_ram.lower()
    palabra = list(palabra_ram.strip(" "))
    palabra.remove("\n")
    return palabra


def consultar_letra(palabra, vidas):
    espacios = len(palabra)
    palabra_jug = "_" * espacios
    letra_jug = input("Ingrese una letra: ").lower()
    i = 0
    for letra in palabra:
        i = i + 1
        if letra_jug == letra:
            palabra_jug = palabra_jug[:i-1] + letra + palabra_jug[i:]
        else:
            vidas = vidas - 1
    print(palabra_jug)
    return vidas


'''def animaciones():
    pass


def menu():
    pass
'''


def run():
    vidas = 3
    palabra = read()
    while vidas > 0:
        consultar_letra(palabra, vidas)
    print(palabra)


if __name__ == "__main__":
    run()