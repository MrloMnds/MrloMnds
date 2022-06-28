# Criptografar #
def cript():
    texto_cript = []
    chave = input('Digite a chave: ')
    texto = input('Digite o texto para criptografar: ')
    for letra in texto:
        letra_cript = ord(letra) + int(chave) + (int(chave)*2)
        texto_cript.append(chr(letra_cript))
    print(*texto_cript, sep='')


# Traduzir #
def descript():
    texto_cript = []
    chave = input('Digite a chave: ')
    texto = input('Digite o texto para descriptografar: ')
    for letra in texto:
        letra_cript = ord(letra) - int(chave) - (int(chave)*2)
        texto_cript.append(chr(letra_cript))
    print(*texto_cript, sep='')


# Escolhe uma das opcoes acima #
resposta = input('Digite 1 para criptografar e 2 para traduzir criptografia: ')
if resposta == '1':
    cript()
elif resposta == '2':
    descript()
else:
    print(f'A resposta {resposta} nao eh valida. Digite 1 ou 2!')
