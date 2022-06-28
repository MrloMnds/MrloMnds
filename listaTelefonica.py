import random
from random import randint


def gera_lista_tel():
    caracteres_especiais = '{''(`~!@$%^&*()_+#-=['']:;|,<>.?/])''}''"'
    lista_telefonica = {}
    telefone = ''
    nomes = ['Vitor', 'Artur', 'Beto', 'Carlos', 'Denis', 'Eduardo', 'Fabio', 'Gabriel', 'Heitor', 'Igor', 'Joao',
             'Kyle', 'Leila', 'Maria', 'Natalia', 'Otavio', 'Paula', 'Rosa', 'Silvana', 'Thiago', 'Ulices',
             'Murilo da Mota', 'Carlos Eduardo Campos', 'Isabel Gomes', 'Joaquim Rezende', 'Erick Farias',
             'Fernanda Monteiro', 'Jose', 'Bruno', 'Lucas', 'Pedro', 'Luciano', 'Diego', 'Rômulo']
    nomes_usados = nomes.copy()
    numeros = []

    # Cria um número de telefone aleatorio e atribue a um nome da lista #
    while True:
        if len(nomes_usados) == 0:
            break
        for n1 in range(7):
            numero = randint(0, 9)
            telefone += str(numero)
            if len(telefone) == 7:
                if numero not in numeros:
                    numeros.append(f'9{randint(8, 9)}{telefone}')
                telefone = ''
        if len(numeros) == len(nomes):
            while True:
                nome_aleatorio = random.choice(nomes_usados)
                numero_aleatorio = numeros[randint(0, len(numeros) - 1)]
                contato = {nome_aleatorio: numero_aleatorio}
                lista_telefonica.update(contato)
                nomes_usados.remove(nome_aleatorio)
                if len(nomes_usados) == 0:
                    print(lista_telefonica)
                    break

    # Checa se o nome procurado esta na lista telefonica e pergunta se deseja procurar mais algum nome #
    while True:
        nome_digitado = (input('Digite o nome da pessoa que procura: '))
        if nome_digitado.title() not in nomes:
            print("O nome que procura n foi encontrado, veja se digitou corretamente.")
            continue
        for k, v in lista_telefonica.items():
            if nome_digitado.lower() == k.lower():
                print(f'{k}: {v}')
        if nome_digitado.isnumeric():
            print('Digite usando apenas letras!')
        for caractere in caracteres_especiais:
            if caractere in nome_digitado:
                print('Digite usando apenas letras!')
        resposta = input('Deseja procurar mais algum nome? (Digite [s] para SIM e [n] para NAO): ')
        if resposta == 's'.lower():
            continue
        elif resposta == 'n'.lower():
            break

