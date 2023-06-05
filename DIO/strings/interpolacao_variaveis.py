
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

pessoa = {"nome": "Guilherme", "idade": 28, "profissao": "Programador", "linguagem": "Python" }


# Old Format : %
print("Ola, me chamo %s. Tenho %d anos de idade, trabalho como %s, e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

# Método Format

# Se usado sem nada dentro ele segue a mesma ordem que são apresentadas as variáveis
print("Ola, me chamo {}. Tenho {} anos de idade, trabalho como {}, e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))
# Com número dentro , representa a variável na posição correspondente
print("Ola, me chamo {3}. Tenho {2} anos de idade, trabalho como {1}, e estou matriculado no curso de {0}." .format(profissao, linguagem, idade, nome))
# Dessa forma é possível determinar "a qual variável" a "variável informada" pertence 
print("Ola, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao}, e estou matriculado no curso de {linguagem}." .format(nome = nome, idade = idade, profissao = profissao, linguagem = linguagem))
# Pegando de algum dicionário
print("Ola, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao}, e estou matriculado no curso de {linguagem}." .format(**pessoa))

# Método f-string

#só coloca o valor dentro das chaves e a letra f antes de tudo
print(f"Ola, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao}, e estou matriculado no curso de {linguagem}.") 
# formatando uma string com f-string

PI = 3.14159
# escreva "valor de PI:" o valor antes do ponto e dois depois
print(f"Valor de PI: {PI: .2f}")
# escreva "Valor de PI:" com 10 casas antes do ponto e duas depois
print(f"Valor de PI: {PI:10.2f}")