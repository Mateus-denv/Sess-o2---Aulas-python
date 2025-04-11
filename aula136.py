# List comprehesion em python
# List comprehension é uma forma rapida para criar lista apartir de interaveis

lista = []
for numero in range(20):
    lista.append(numero)
    
lista = [numero * 2 for numero in range (10)] # Adiciona um valor na lista e multiplica por um valor deseijado

print(lista)
print(list(range(10)))

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1','Valor': 20,},
    {'nome': 'p2','Valor': 10,},
    {'nome': 'p3','Valor': 56,},
    {'nome': 'p4','Valor': 18,},
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(novos_produtos)
print(*novos_produtos, sep='\n')