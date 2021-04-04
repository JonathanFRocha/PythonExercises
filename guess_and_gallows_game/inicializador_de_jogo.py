import adivinhacao
import forca

print("*******************************")
print("****** Choose your Game *******")
print("*******************************")


game = int(input("choose your game 1-Adivinhação 2-Forca: "))


if game == 1:
    print("lets go to Adivinhação!")
    adivinhacao.jogar()
elif game == 2:
    print("lets go to Forca!")
    forca.jogar()
