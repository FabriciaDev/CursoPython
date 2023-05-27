#função built-in range
# range(stop) -> range object
# range(start, stop[,step]) -> range object

# ex
# list(range(4))
# >>> [0,1,2,3]

#printa uma lista de 0 a 10

for numero in range(0, 11):
    print(numero, end=" ")

#exibe a tabuada do 5

for numero in range(0, 51, 5):
    print(numero, end=" ") # colocando o end forçamos os caracteres a serem colocados lado a lado   