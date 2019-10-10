#Autor: Yuri Pereira Dantas
#Data: 01/10/2019
#
#Descricao: questao 4 da P1 de comp1

def nob(num_a, num_b):
    sizeA = len(num_a)
    sizeB = len(num_b)
    numA1 = num_a[0]
    numB1 = num_b[0]
    numA1 = int(numA1)
    numB1 = int(numB1)
    if sizeA == 1 and sizeB == 1:
        resposta = numA1 + numB1
        return resposta
    elif sizeA == 1 and sizeB == 2:
        numB2 = num_b[1]
        numB2 = int(numB2)
        resposta = numA1 + numB1 +numB2
        return resposta
    elif sizeA == 2 and sizeB == 1:
        numA2 = num_a[1]
        numA2 = int(numA2)
        resposta = numA1 + numA2 + numB1
        return resposta
    elif sizeA == 2 and sizeB == 2:
        numA2 = num_a[1]
        numB2 = num_b[1]
        numA2 = int(numA2)
        numB2 = int(numB2)
        resposta = numA1 + numB1 + numA2 + numB2
        return resposta

def main():
    a = input('Digite um inteiro')
    b = input('Digite outro inteiro')
    resultado = nob(a,b)
    print('O resultado e', resultado)

main()

#QUESTAO CERTA PELO O QUE EU CONFERI AQUI
    
    
