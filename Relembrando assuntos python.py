# Relembrando assuntos python
"""
## Tipos de operadoes
### Operadores aritméticos
print("Operadores aritméticos")

produto1 = 10
produto2 = 20

print(produto1 + produto2)
print(produto1 - produto2)
print(produto1 * produto2)
print(produto1 / produto2)
print(produto1 // produto2)
print(produto1 % produto2)
print(produto1 ** produto2)

### Ordem de execução
print("\nOrdem de execução")

#        10    +    20    -    10    *    20
print(produto1 + produto2 - produto1 * produto2)
#        10    +    20    -    10    *    20
print(produto1 + produto2 - ((produto1 * produto2) // produto1 % produto2))

### Operadores de atribuição

print("\nOperadores de atribuição")

saldo1 = 200
saldo1 += 200
print(saldo1)

saldo2 = 100
saldo2 //= 2
print(saldo2)

saldo3 = 500
saldo3 *= 2
print(saldo3)

saldo4 = 12
saldo4 **= 2
print(saldo4)

### Operadores de Lógicos
print("\nOperadores Lógicos")

valor1 = 10
valor2 = 20
valor3 = 30

print("1-",valor1 < valor2)
print("2-",valor2 >= valor3)
print("3-",valor2 < valor2 or valor3 == valor1)
print("4-",valor1 == valor1 and valor3 > valor1)
print("5-",not 1000 > 1500) # o NOT inverte o resultado do boolean

contatos_emergencia = [] # Uma lista vazia é false
print("6-",not contatos_emergencia)

print("7-",not "Saque 1500") # Uma string com valor é TRUE

print("8-", (valor1 == valor1) and (valor2 < valor3) or (valor2 > valor3))

### Operadores de identidade
print("\nOperadores de identidade")

saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)

### Operadores de associação
print("\nOperadores de associação")

curso = "Curso de Python"
frutas = ["Laranja","uva", "limão"]
saques = ["100","200"]

print('Python' in curso)
print('Laranja' not  in curso)
print('200' in saques)

""" 
