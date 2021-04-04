import random


def jogar():

    print_mensagem_bemvindo()

    palavra_secreta = carregar_palavra_aleatoria()

    lista_de_letras = inicializa_palavra_secreta(palavra_secreta)
    print(lista_de_letras)
    acertou = False
    enforcou = False
    erros = 0

    while not acertou and not enforcou:
        index = 0
        letra_chutada = input("Tente uma letra: ").strip().upper()
        if letra_chutada in palavra_secreta:
            for letra in palavra_secreta:
                if letra_chutada == letra:
                    lista_de_letras[index] = letra
                index += 1
            acertou = "_" not in lista_de_letras
        else:
            erros += 1
            desenha_forca(erros)
            enforcou = erros == 7

        print(lista_de_letras)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def print_mensagem_bemvindo():
    print("*******************************")
    print("Bem vindo ao jogo da forca!")
    print("*******************************")


def carregar_palavra_aleatoria():
    palavras = open("palavras.txt", "r")

    lista_de_palavras = []
    for linha in palavras:
        linha = linha.strip()
        lista_de_palavras.append(linha)

    palavras.close()

    index_aleatorio = random.randrange(0, len(lista_de_palavras))

    palavra_secreta = lista_de_palavras[index_aleatorio].upper()
    return palavra_secreta


def inicializa_palavra_secreta(palavra):
    return ["_" for letra in palavra]


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()