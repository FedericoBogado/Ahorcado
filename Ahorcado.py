import random


def read():
    list_pal = []
    with open("./Data.txt", "r", encoding="UTF-8") as f:
        for palabras in f:
            list_pal.append(palabras)
    palabra_ram = random.choices(list_pal)
    palabra_ram = "".join(palabra_ram)
    palabra_ram = palabra_ram.lower()
    palabra_ram = switch(palabra_ram)
    palabra = list(palabra_ram.strip(" "))
    palabra.remove("\n")
    return palabra


def switch(palabra_ram):
    i = 0
    for letra in palabra_ram:
            i = i + 1
            if letra == "á":
                palabra_ram = palabra_ram[:i-1] + "a" + palabra_ram[i:]
            elif letra == "é":
                palabra_ram = palabra_ram[:i-1] + "e" + palabra_ram[i:]
            elif letra == "í":
                palabra_ram = palabra_ram[:i-1] + "i" + palabra_ram[i:]
            elif letra == "ó":
                palabra_ram = palabra_ram[:i-1] + "o" + palabra_ram[i:]
            elif letra == "ú":
                palabra_ram = palabra_ram[:i-1] + "u" + palabra_ram[i:]
            elif letra == "ü":
                palabra_ram = palabra_ram[:i-1] + "u" + palabra_ram[i:]
            else:
                pass
    return palabra_ram


def mecanica_principal(palabra, palabra_list):
    vidas = 3
    espacios = len(palabra_list)
    palabra_jug = "_" * espacios
    while vidas > 0:
        letra_jug = input("\nIngrese una letra: ").lower()
        i = 0
        acerto = False
        for letra in palabra_list:
            i = i + 1
            if letra_jug == letra:
                palabra_jug = palabra_jug[:i-1] + letra + palabra_jug[i:]
                acerto = True
            else:
                pass
        if acerto == False:
            vidas = vidas - 1
        elif palabra == palabra_jug:
            print("\nGanaste wachin\n")
            exit()
        else:
            pass
        print("\n" + palabra_jug)


'''def animaciones():
    pass'''


def menu(palabra, palabra_list):
    dec = input("1] Jugar\n2] Salir\n\n")
    if dec == "1":
        mecanica_principal(palabra, palabra_list)
    elif dec == "2":
        exit()


def run():
    palabra_list = read()    
    palabra = "".join(palabra_list)
    print(palabra_list)
    menu(palabra, palabra_list)


if __name__ == "__main__":
    run()