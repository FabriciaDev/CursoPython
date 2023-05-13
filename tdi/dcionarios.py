# Dicionários são compostos da chave e do valor. Chaves são as variávei dentro de um dicionártio

# pode-se fazer uma lista de dicionários
# a lista é fechada na lina em que foi aberta
alvo = [ {'ip': '192.168.1.1', 'so': "windows", 'ativo': True, 'portas': [80, 22, 21]},  {'ip': '192.168.1.1', 'so': "linux", 'ativo': False, 'portas': [4444, 2222, 21]}, {'ip': '192.168.1.1', 'so': "windows", 'ativo': False, 'portas': [80]}, {'ip': '192.168.1.1', 'so': "os", 'ativo': False, 'portas': [3306, 1337]} ]
# todos
print(alvo)
# terceiro item da lista de dicionários que tenha a chave portas
print(alvo[3]["portas"])
# segundo item da lista de dicionários que tenha a chave so
print(alvo[2]["so"])

# brincando com dicionários

alvo = {'ip': '192.168.1.1', 'so': "windows", 'ativo': True, 'portas': [80, 22, 21] }
# adicionando uo atualizandoi um valor ( se o valor não existir ele cria)
print(alvo)
del alvo["so"] 
print(alvo)

# remover um item do dicionario
print(alvo)
alvo["so"] = "linux"
print(alvo)
