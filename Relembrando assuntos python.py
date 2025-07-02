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
