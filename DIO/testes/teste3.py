#a variável mounth recebe um input trasformado em inteiro
month = int(input(''))
# criado dicionario
months_dict = { 1 : 'January', 2 : 'February', 3 : 'March', 4 : 'April', 5 : 'May', 6 : 'June', 7 : 'July', 8 : 'August', 9 : 'September', 10 : 'October', 11 : 'November', 12 : 'December',}
# se month está dentro do dicionário months_dict faça
if month in months_dict:
# escreva o equivalente a variável month do dicionário    
    print(months_dict[month])