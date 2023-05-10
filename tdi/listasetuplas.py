# IPs são "Strings"
# o primeiro item de uma lista é o zero!!!! ou seja os itens estão nas posições 0,1,2...

alvos = ["192.168.1.20" , "192.168.1.20" , "192.168.1.40"]

# ler ou acessar uma lista

print(alvos[2]) # printa a lista na posição 2

print(alvos [-2]) # printa a lista na posição -2, ou seja, lendo de trás para frente

print(alvos[0:2]) # printa a lista da primeira posição áté a posição determinada 

# adicionar um elemento a uma lista (adicionado sempre no final da lista)

alvos.append("185.123.1.40")
print("alvos")

# adiciobnar umn elemento a uma posição específica na rede
            #posição seguido do item acrescentado
alvos.insert(0, "inicio")

# remover
alvos.remove("inicio")
print(alvos)

# remove o último elemento de uma lista e guarda em uma variável

ultimo = alvos.pop()
print(alvos)
print(ultimo)

# verifica o tamnho de uma  lista
print(len(alvos))

#verifica se um elemento está ou não contido em uma lista (retorna booleano)
print("192.168.1.20" in alvos)
print("inicio" not in alvos)

#tuplas são listas que são imutáveis como as "variaveis constantes" ou seja, só permite leitura dife3rem no caracter especial 

tupla = ("vaca", "galinha", "cachorro")
