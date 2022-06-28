from random import randint
valores = []
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

# Give a random number of "points" to each letter in the alphabet #
for item in alfabeto:
    valores.append(randint(1, 10))

# Starts the game #
while True:
    print('Digite uma palavra: ')
    player1 = input('\tPlayer 1: ')
    player2 = input('\tPlayer 2: ')
    pontos1 = 0
    pontos2 = 0
    indices = []

    # player1 points #
    for letra in player1:
        letra = letra.upper()
        if letra in alfabeto:
            indices.append(alfabeto.index(letra))
    for num in indices:
        pontos1 += valores[num]

    # player2 points #
    for letra in player2:
        letra = letra.upper()
        if letra.upper() in alfabeto:
            indices.append(alfabeto.index(letra))
    for num in indices:
        pontos2 += valores[num]

    # Show results and declare winner #
    print('')
    print(f'Player 1: {pontos1} pontos.')
    print(f'Player 2: {pontos2} pontos.')
    print('')
    print('Resultados:')
    if pontos1 > pontos2:
        print('Player 1 eh o vencedor!')
    elif pontos2 > pontos1:
        print('Player 2 eh o vencedor!')
    elif pontos2 == pontos1:
        print('Empate!')

    # Asks if you want to continue playing #
    resposta = input('Jogar novamente? Responda sim ou nao: ')
    if 's' in resposta or 'S' in resposta:
        print('')
        continue
    elif 'n' in resposta or 'N' in resposta:
        print('')
        break
    else:
        print(f'Resposta "{resposta}" eh invalida.')
        break
