from random import randint


def gerador_cpf():
    numero = str(randint(100000000, 999999999))
    cpf = numero
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9
        total += int(cpf[index])*reverso

        reverso -= 1

        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)
            if digito > 9:
                digito = 0
            total = 0
            cpf += str(digito)

    print(cpf)
