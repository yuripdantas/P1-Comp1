#Autor: Yuri Pereira Dantas
#Data:01/10/2019
#
#Descricao: Programa da questao 1 da P1 de computacao 1 do jeito que escrevi na prova

from math import sqrt #() 
def raizes(a,b,c):
    delta = ((b*b)-(4*a*c))
    if delta < 0:
        real = -b/(2*a)
        imaginario = (sqrt(-delta)/(2*a))
        print('As raizes sao:', real, '+', imaginario , 'i')
        print('e', real, '-', imaginario, 'i')
        return 1
    elif delta == 0:
        raizUnica = -b/(2*a)
        print('A raiz e', raizUnica)
        return 0
    else:
        raiz1 = (-b+sqrt(delta))/(2*a)
        raiz2 = (-b-sqrt(delta))/(2*a)
        print('As raizes sao:', raiz1, 'e', raiz2)
        return 0
    #EU ESQUECI DE BOTAR PRA FUNCAO PEDIR OS COEFICIENTES BURRO

