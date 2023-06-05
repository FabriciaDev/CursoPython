# fatiamento de string é uma técnica usada para retornar substrings
# inicio(start) fim(stop) e passo(step): [start: stop[, step]]

nome = "Guilherme Arthur de Carvalho"

# retorna a posição selecionada
print(nome[0])
# retorna os valores até aquela posição
print(nome[:9])
# retorna os valores daquela posição até o final
print(nome[10:])
# retorna os valores entre as posições
print(nome[10:16])
# retorna os valores entre as posições com o intervelo descrito
print(nome[10:16:2]) 
# retorna uma cópia da variável
print(nome[:])
# deixando os primeiros itens em branco e dando ao steo o valor -1 temos o espelhamento da string
print(nome[:: -1])
