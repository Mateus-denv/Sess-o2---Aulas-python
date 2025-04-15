#  Filtro de dados em list comprehension (filter)
# Tudo que vem esquerda do for é mapeamento tudo que vem a direta do for é filtro
lista = [Numero for Numero in range(10) if Numero > 2]
print(lista)