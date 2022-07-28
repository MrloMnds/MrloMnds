while True:
    cpf = input('Digite seu CPF: ')
    if not cpf.isnumeric():
        print('Digite apenas numeros!')
        continue
    if len(cpf) < 11:
        print('O CFP que digitou eh muito curto.')
        continue
    cpf2 = cpf[:-2]
    reverso = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9
        total += int(cpf2[index])*reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)
            if digito > 9:
                digito = 0
            total = 0
            cpf2 += str(digito)
    sequencia = cpf2 == str(cpf2[0])*len(cpf)  # checa se o cpf2 eh uma repeticao do primeiro numero
    if cpf2 == cpf and not sequencia:
        print('CPF valido.')
        return True
    else:
        print('CPF invalido.')
        return False
