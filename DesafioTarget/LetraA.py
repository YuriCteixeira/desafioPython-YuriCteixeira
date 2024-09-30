#Questão 2 - Ocorrência da letra "a" e "A"
#Verificando quantos "as" aparecem
def verificador(word):
    contagem = word.lower().count('a')
    return contagem

#Input
texto = input('Informe seu texto: ')

#Quantidade de "as"
qtde = verificador(texto)

#Tem "a" no texto? Quantos?
if qtde == 0:
    print('Não tem vogal "a/A" no seu texto')
else:
    print('A vogal "a/A" aparece {} vez(es) no seu texto'.format(qtde))
