# aritméeticods

# adição
print(1 + 1)

#subtração
print(10 - 2)

# multiplicação
print(4 * 3)

#divisão
print(6 / 3)

# divisão inteira
print(9 // 4)

# módulo: o resto da divisão
print(2 ** 3)

# exponenciação
print(2 ** 3)

# ordem matemática
# 1.Parêntesis
# 2.Expoentes
# 3.Multiplicações e divisões (da esquerda para a direita)
# 4.Somas e subtração (da esquerda para a direita)

# operadores de comparação

saldo = 450
saque = 200
# maior que
print(saldo > saque)
# menor que
print(saldo < saque)
# #igualdade
print(saldo == saque)
#diferente
print(saldo != saque)
#maior ou igual a
print( saldo >= saque)
#menor ou igual a 
print(saldo <= saque)

# operadores de atribuição

# saldo recebe 200
saldo = 200
# saldo recebe saldo + 200
saldo += 200
# saldo recebe saldo - 100
saldo -= 100
# saldo recebe saldo na potencia 5
saldo *= 5
# saldo recebe saldo com 5 por cento
saldo %= 5
print(saldo)

#operadores lógicos
saldo = 1000
saque = 200
limite = 100
#or
print(saldo >= saque or saque <= limite)
#not 
print(not(saldo >= saque or saque <= limite))
#and
print(saldo >= saque and saque <= limite)

#operadores de identidade
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

#is
print(curso is nome_curso)
print(saldo is limite)
#is not
print(curso is not nome_curso)

# operadores de associação

curso = "Curso de Python"
frutas = ["banana", "laranja, uva"]
saques = [1500, 100]

#in
print("Python" in curso)
#not in 
print("maça" not in frutas)
          

