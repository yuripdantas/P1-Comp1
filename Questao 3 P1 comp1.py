#Autor: Yuri Pereira Dantas
#Data: 01/10/2019
#
#Descricao: Questao 3 da P1 de Comp1

acumulador = 0
diferenca = 10 #so para diferenca ser maior que a condicao do looping
n = 1
b = 0
fator = 1
while diferenca > (5*(10**-8)):
    a = (fator * 1/n)
    fator = fator*(-1)
    n = n + 2
    diferenca = a - b
    b = a
    if diferenca < 0:
        diferenca = (-1)*diferenca
    acumulador = a + acumulador
pi = 4 * acumulador
print('O valor de pi é', pi)

#Cheguei em casa, testei e parece que esta tudo certo
