import forca
import adivinhacao

def escolhe_jogo():
    print('<----------------------------->')
    print('-------Escolha seu Jogo--------')
    print('<----------------------------->')

    print('Qual jogo você deseja jogar?')
    print('(1) Forca | (2) Adivinhação')

    jogo = int(input('Escolha: '))

    if (jogo == 1):
        print('Jogando forca')
        forca.jogar()
    elif (jogo == 2):
        print('Jogando adivinhação')
    adivinhacao.jogar()
if (__name__ == '__main__'):
    escolhe_jogo()