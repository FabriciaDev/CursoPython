# comolfazer uma função em Python

def hello(name):
    print("hello world " + name)
    
hello("Bruno")    

# a função exemplo tem como objetivo receber email e senha do aluno, fazer o loguin e ddar boas vindas

def fazer_login(login, senha):
    print("Bem vindo ")
    print("usuario: " + login)

fazer_login("tdi@tdi.com", 123)    

# exemplo de função com return

def plus(n1, n2):
    return n1 + n2

resultado = plus(10, 10)
print(resultado)

#IMPORTANTE: NÃO EXISTE VIDA DEPOIS DO RETURN! Quando colocada o return em um função a função acaba 

#exemplo 2

def add_https(dominio, nome):
    juntar = "https://www." + dominio + " entendeu " + nome 
    return juntar

print(add_https("tecnicasdeinvasao.com", "Bruno"))

print(add_https("globo.com", "Bruno"))

# Keyword Argument: a ordem dos tratores não altera a rodovia
print(add_https(nome="Brumo", dominio="www.com"))