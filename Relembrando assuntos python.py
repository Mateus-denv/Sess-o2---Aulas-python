# Relembrando assuntos python
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

