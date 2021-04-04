import random


def jogar():
    print("*******************************")
    print("Try to guess the secret number!")
    print("*******************************")

    pontos = 1000
    secretNumber = random.randrange(0, 101)
    total_de_tentativas = 0

    print(5.3 // 2)

    dificuldade = int(input("Choose your difficulty 1-easy 2-normal 3-hard: "))
    if dificuldade == 1:
        total_de_tentativas = 20
    elif dificuldade == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("rodada {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Type your guess:"))
        if chute < 0 or chute > 100:
            print("Seu chute tem de ser entrem 0 e 100")
            continue

        acertou = chute == secretNumber
        maior = chute > secretNumber
        menor = chute < secretNumber

        if acertou:
            print("acertou e fez {} pontos".format(pontos))
            break
        elif maior:
            print("maior")
        else:
            print("menor")
        pontos_perdidos = abs(secretNumber - chute)
        pontos = pontos - pontos_perdidos


if __name__ == "__main__":
    jogar()