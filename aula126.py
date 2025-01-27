# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

"""
s1 = set('Luiz')
#s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados
print(s1)
"""

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

"""l1 = [1,2,3,2,1,3]
print(l1)
s1 = set(l1)
l1 = list(s1)
print(8 in l1)"""

# Métodos úteis:
# add, update, clear, discard

"""
s1 = set()
s1.add('Luis')
s1.add(1)
s1.update(('OI',))
s1.discard('OI')
print(s1)
"""

# Operadores úteis:

s1 = {1,2,7}
s2 = {2,7,5}

# união | união (union) - Une
s3 = s1 | s2
print(s3)
# intersecção & (intersection) - Itens presentes em ambos
s4 = s1 & s2
print(s4)
# diferença - Itens presentes apenas no set da esquerda
s5 = s1 - s2
print(s5)
# diferença simétrica ^ - Itens que não estão em ambos
s6 = s1 ^ s2
print(s6)
