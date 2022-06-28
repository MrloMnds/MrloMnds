while True:

    # validador de CPF #
    while True:
        cpf = input('Digite seu CPF: ')
        try:
            int(cpf)
        except ValueError:
            print('Digite apenas numeros!')
            continue
        if len(cpf) < 11:
            print('O CPF que digitou eh muito curto.')
            continue
        cpf2 = cpf[:-2]
        reverso = 10
        total = 0
        for index in range(19):
            if index > 8:
                index -= 9
            total += int(cpf2[index]) * reverso
            reverso -= 1
            if reverso < 2:
                reverso = 11
                digito = 11 - (total % 11)
                if digito > 9:
                    digito = 0
                total = 0
                cpf2 += str(digito)
        sequencia = cpf2 == str(cpf2[0]) * len(cpf)  # checa se o cpf2 eh uma repeticao do primeiro número
        if cpf2 == cpf and not sequencia:
            print('CPF valido.')
            break
        else:
            print('CPF invalido.')
            continue

    # Variaveis #
    total_candidatos = int(input('Numero de candidatos: '))
    total_eleitores = int(input('Numero de eleitores: '))
    candidatos = {}
    i = 1
    i2 = 1
    num_votos = 0
    total_votos = {}
    soma_votos = 0

    while True:
        # Inserindo candidatos #
        while i <= total_candidatos:
            nome = input('Digite o nome do candidato: ')
            num = input('Digite o numero do candidato: ')
            int(num)
            candidato = {nome: int(num)}
            candidatos.update(candidato)
            votos = {int(num): num_votos}
            total_votos.update(votos)
            i += 1

        # Inserindo votos #
        while i2 <= total_eleitores:
            voto = input('Digite o numero do candidato em que deseja votar: ')
            for numero in candidatos.values():
                if int(voto) == numero:
                    for n in total_votos.keys():
                        if int(voto) == n:
                            total_votos[n] += 1
            i2 += 1
        print('')

        # Organizando informacoes e resultados #
        print('Resultados: ')
        for value in sorted(total_votos, key=total_votos.get, reverse=True):
            soma_votos += total_votos[value]
        for value in sorted(total_votos, key=total_votos.get, reverse=True):
            porcentagem = total_votos[value]/soma_votos*100
            print(f'\tO candidato de numero {value}, obteve {total_votos[value]} votos.\n\tCorrespondente a '
                  f'aproximadamente {porcentagem:.2f}% dos votos.')
        print('')
        for value in sorted(total_votos, key=total_votos.get, reverse=True):
            print(f'\tCandidato de numero {value} foi eleito com {total_votos[value]} votos.')
            break
        break
    break
