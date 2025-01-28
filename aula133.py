# Função Lambda em Python
# A função lambda é uma função como qualquer outra em python.
# Outra em Python, Porém, são funções anônimas que contem apenas uma linnha. Ou seja, tudo deve ser contido dentro de uma unica expressão.

"""lista_numero = [1,2,3,4,5,67,8,9]
lista_numero.sort(reverse=False)
print(lista_numero)
"""

lista = [
    {
        'nome' : 'Luiz', 'sobrenome' : 'Miranda'
    },
    {    
        'nome' : 'Matheus', 'sobrenome' : 'Costa'
    }
]


"""def ordena(nome):
    return nome['nome']


lista.sort(key=ordena)"""

# lista.sort(key=lambda item: item['nome'])

l1 = sorted(lista, key=lambda nome: nome['nome'])
l2 = sorted(lista, key=lambda nome: nome['sobrenome'])


def exibir(lista):
    for intem in lista:
        print(intem)
    print()

exibir(l1)
exibir(l2)