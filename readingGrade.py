caracteres_especiais = '{''(`~!@$%^&*()_+#-=['']:;|,<>.?/])''}''"'
palavras = 1
letras = 0
frases = 0
palavra = ''
while True:
    paragrafo = input('Digite uma parte de um livro: ')
    while len(paragrafo) <= 0:
        paragrafo = input('Digite uma parte de um livro: ')
    for letra in paragrafo:  # contador de letras/palavras e formador de lista_palavras
        if not letra.isspace() and letra not in caracteres_especiais:
            letras += 1
            palavra += letra
        if letra.isspace():
            palavras += 1
            palavra = ''
        if letra == '.' or letra == '!' or letra == '?':
            frases += 1
        if paragrafo.startswith(' '):
            palavras -= 2
    l_ = (letras * 100) / palavras
    f_ = (frases * 100) / palavras
    formula = 0.0588 * l_ - 0.296 * f_ - 15.8
    palavras = 1
    letras = 0
    frases = 0
    if round(formula) < 1:
        print('Grau de leitura abaixo de 1.')
    elif 1 < round(formula) < 18:
        print(f'Grau de leitura {round(formula)}.')
    elif round(formula) >= 18:
        print('Grau de leitura maior que 18.')
    resposta = input('Deseja fazer mais algum teste? Digite [s] para sim e [n] para nao: ')
    if resposta == 'S' or resposta == 's':
        continue
    elif resposta == 'N' or resposta == 'n':
        print('Finalizado')
        break
    else:
        print('Digite uma resposta valida!')
    break
