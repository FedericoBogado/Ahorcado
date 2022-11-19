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


def mecanica_principal(palabra, palabra_list, imagenes):
    intentos = 0
    espacios = len(palabra_list)
    palabra_jug = "_" * espacios
    letras = []
    while intentos < 6:
        print(imagenes[intentos] + "\n")
        letra_jug = input("\nIngrese una letra: ").lower()
        assert letra_jug.isalpha(), "Tiene que ser una letra culiado"
        assert len(letra_jug) == 1, "Una sola letra culiado"
        if letra_jug in letras:
            print("\n!!!YA USASTE ESA LETRA WACHIN!!!")
        else:
            pass
        letras.append(letra_jug)
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
            intentos = intentos + 1
        elif palabra == palabra_jug:
            print("\nGanaste wachin\n")
            print("La palabra era: " + palabra + "\n")
            exit()
        else:
            pass
        print("\n" + palabra_jug)
    if intentos == 6:
        print("\n\nPerdiste wachin")
        print(imagenes[intentos] + "\n")
        print("AHORCADO!\n")
        print("La palabra era: " + palabra + "\n")



def menu(palabra, palabra_list, imagenes):
    opc = ("1", "2")
    dec = input("\n1] Jugar\n2] Salir\n\n")
    assert dec in opc, "Tiene que ser una de las opciones culiado"
    if dec == "1":
        mecanica_principal(palabra, palabra_list, imagenes)
    elif dec == "2":
        exit()


def run():
    palabra_list = read()    
    palabra = "".join(palabra_list)
    imagenes = ['''
   +---+

   |   |

       |

       |

       |

       |

 =========''', '''

   +---+

   |   |

   O   |

       |

       |

       |

 =========''', '''

   +---+

   |   |

   O   |

   |   |

       |

       |

 =========''', '''

   +---+

   |   |

   O   |

  /|   |

       |

       |

 =========''', '''

   +---+

   |   |

   O   |

  /|\  |

       |

       |

 =========''', '''

   +---+

   |   |

   O   |

  /|\  |

  /    |

       |

 =========''', '''

   +---+

   |   |

   O   |

  /|\  |

  / \  |

       |

 =========''']
    #print(palabra_list)
    menu(palabra, palabra_list, imagenes)


if __name__ == "__main__":
    run()