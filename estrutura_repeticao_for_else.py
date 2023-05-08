# no exemplo a variável recebe um número do teclado e retorna  o próprio número e os seguintes
# exemplo sem estrutura de repeticao

a = int(input("Informe um número inteiro"))
print(a)

a+= 1
print(a)

a+= 1
print(a)

# for: para percorrer um objeto 

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"
#GERALMETE VARIÁVEIS EM LETRA MAIÚSCULA SÃO CONSTANTES

for letra in texto:
    if letra.upper() in VOGAIS: #upper trasforma em maiúscula
        print(letra, end="")

# for/for else
else:        
    print("não foram encontradas vogais")
