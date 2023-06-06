#N recebe o imput como inteiro
N = int(input())

# para a quantidade de itens informad pela variável N faça
for _ in range(N):
    # as variaáveis A e B recebem um imput, retiram os espaços em branco ndo início e final e subdividindo a string
    A, B = input().strip().split(' ')
    # se a contagem de B for maior que A faça
    if(len(B) > len(A)):
        # escreva nao encaixa
        print('nao encaixa')
    # se não
    else:
        #a recebe A somente com o que encontrar em B
        A = A[(len(A) - len(B)):]
        # se A for igual B 
        if A == B:
           # escreva encaixa
           print('encaixa')
        # se naõ
        else:
            #escreva
            print('nao encaixa')