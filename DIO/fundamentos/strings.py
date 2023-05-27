# Maiúscula, minùscula e  título
curso = "   pHaYThoN   "

print(curso)
# em maiúscula
print(curso.upper()) 
# em minúscula
print(curso.lower())
# só com a primeira letra maiúscula
print(curso.title())

# Eiminando espaços em branco
# Eliminando os espaços em bnrnco dos dois lados
print(curso.strip())
# Eliminando os espaços em branco iniciais
print(curso.lstrip())
# Eliminando os espaços em branco finais
print(curso.rstrip())

# método center: o segundo valor é opicional, ou seja se não colocar ele adiciona um espaço
print(curso.center(10, "*"))

# métdo join
print(".".join(curso))

