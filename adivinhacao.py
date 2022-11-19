def jogar():
    print('<----------------------------->')
    print('Bem vindo ao jogo de advinhação')
    print('<----------------------------->')
    import random

    numero_secreto = round(random.randrange(1, 101))
    n_tentativas = 0
    pontos = 1000
    pontos_perdidos = 0
    print('Qual o nível de dificuldade desejada?')
    print('(1) Fácil | (2) Médio | (3) Difícil')
    lvl = int(input('Digite o valor do nível: '))

    if lvl == 1:
        n_tentativas = 10
    elif lvl == 2:
        n_tentativas = 5
    else:
        n_tentativas = 3

    for tentativas in range(1, n_tentativas + 1):
        chute = int(input('Digite seu número entre 1 e 100: '))
        print('você digitou', chute)
        print(tentativas, '° tentativa')
        if (chute < 1 or chute > 100):
            print('Você deve digitar um valor entre 1 e 100!!!')
            continue

        acertou = chute == numero_secreto
        maior   = chute  > numero_secreto
        menor   = chute  < numero_secreto

        if(acertou):
            print('você acertou')
            print(f'total de pontos: {pontos}')
            break
        else:
            if(maior):
                print('chute MAIOR que o número secreto')

            elif(menor):
                print('chute MENOR que o número secreto')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    if n_tentativas == tentativas and chute != numero_secreto:
        print(f'o número secreto era {numero_secreto}')
        print('total de pontos: 0')

    print('\n fim de jogo')

if (__name__ == "__main__"):
    jogar()