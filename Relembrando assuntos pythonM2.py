# Relenbrando assuntos python modulo 2

## Listas
"""print("\nListas\n")

frutas = ["Laranja","Maçã"]

frutas = []

letras = list("Python")

print(frutas)
print(letras)

matriz = [
    [1, "a", 2],
    ["8", "d", 6],
    [4, "y", "c"]
    ]

print (matriz[0])
print (matriz[1][0])

lista = ["p","y","t","h","o","n"]

print(lista[2:])
print(lista[:2])
print(lista[2:1])
print(lista[1:1:1])
print(lista[::-1])

carro = ["gol", "cruze", "argo"]
for indice, modelo in enumerate(carro):
    print(f"{indice}: {modelo}")
    
### Filtro de verção
print("\nFiltro de verção\n")

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

### Compreenção de listas
print("\nCompreenção de listas\n")

pares_ = [numero for numero in numeros if numero % 2 == 0]
print(pares_)

numeros_2x = [numero ** 2 for numero in numeros ]
print(numeros_2x)

lista_8 = [(n**2 if n > 6 else n) for n in range(10) if n % 2 == 0] 
print(lista_8)
"""
