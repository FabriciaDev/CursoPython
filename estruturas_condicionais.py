#estrutura cpondicional if

import sys


saldo = 2000.0
saque = float(input("informe o valor do saque"))

if saldo >= saque:
    print("Realizando saque")

if saldo <= saque:
    print("saldo insuficiente")

# estruturas condicionais if e else 

saldo = 2000.0
saque = float(input ("informe o valor do saque"))

if saldo >= saque:
    print("saque realizado!")

else:
    print("saldo insuficiente!")   

# quando precisa do elif

opcao = int(input ('Informe a opção [1] Sacar ou [2] Extrato'))

if opcao == 1:
    valor = float(input("informe quantia para saque"))
    
elif opcao == 2:   
    print("exibindo o extrato...")
    
else:
    sys.exit("opção inválida!")   
     
#if alinhado: dentro das estruras podem existir vários blocas de if/else com ou sem elif

#if ternário
 
status = "sussesso" if saldo >= saque else "falha" 

print(f"{status} ao realizar o saque!" ) 
#o f concatena  variável status com o resto da string
