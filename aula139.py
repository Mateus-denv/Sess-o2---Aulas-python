"""lista = []
for i in range(2):
    for y in range(10):
        lista.append((i,y))
"""
"""lista = [
    (x,y)
    for x in range(3)
    for y in range(3)
]"""

lista = [
    [(x, letra) for letra in "Mateus"]
    for x in range(3)
]
print(lista)
