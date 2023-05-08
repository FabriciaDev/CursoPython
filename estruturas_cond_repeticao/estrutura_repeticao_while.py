# estrutura de repetição while (enquanto)
opcao = -1

while opcao != 0:
    opcao = int(input("[1] sacar \n[2] extrato \n[0] sair \n:"))
    # o \n pula uma linha
    if opcao == 1:
        print("Sacando...")

    elif opcao == 2:
        print("Exibindo extrato")

else:
    print("obrigado e vote sempre!")            