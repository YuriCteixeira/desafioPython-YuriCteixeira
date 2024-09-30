#Questão 1 - Fibonacci
#O número pertence à Equação de Fibonacci?
def verificador(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

#Input
numero = int(input('Informe um número: '))

#Print
if verificador(numero):
    print('O número {} pertence à equação de Fibonacci!'.format(numero))
else:
    print('O número {} NÃO pertence à equação de Fibonacci!'.format(numero))