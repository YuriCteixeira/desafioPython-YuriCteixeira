#Questão 4 - Completar Lógica
import math
#a) 1, 3, 5, 7, ___
numeros1 = []
for i in range(1, 10, 2):
    numeros1.append(i)
print(numeros1)
print('O próximo número é {}'.format(numeros1[4]))

#b) 2, 4, 8, 16, 32, 64, ____
numeros2 = []
termo = 1
for j in range(7):
    termo *= 2
    numeros2.append(termo)
print(numeros2)
print('O próximo número é {}'.format(numeros2[5]))
#c) 0, 1, 4, 9, 16, 25, 36, ____
numeros3 = []
termo2 = 0
for l in range(0, 8):
    termo2 = math.pow(l, 2)
    numeros3.append(termo2)
print(numeros3)
print('O próximo número é {}'.format(numeros3[7]))

#d) 4, 16, 36, 64, ____
numeros4 = []
termo3 = 4

for m in range(4, 12, 2):
    numeros4.append(math.pow(m, 2))
print(numeros4)
print('O próximo número é {}'.format(numeros4[3]))

#e) 1, 1, 2, 3, 5, 8, ____
termo4 = 9
a, b = 0, 1
while a < termo4:
    a, b = b, a + b
print('O próximo número é {}'.format(a))

# 2,10, 12, 16, 17, 18, 19, ____
print('A resposta é 200. Todos os números começam com a letra "d"')