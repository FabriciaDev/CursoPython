entrada = '' # é declarada a variável de entrada.
# Depois é inserido o método de input para receber a informação.
entrada = input( "Digite uma frase de no máximo 10 caracteres: " )
# Apenas para demostrar é contato os caracteres da variável
tamanho = len ( entrada )
#limita a variável com a quantidade de caracteres específica
saida = entrada [ 0:10]
#saida dos dados
print("A informação de entrada tinha ", tamanho," e a saída ficou: ", saida)
