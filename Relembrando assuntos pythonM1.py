# Relembrando assuntos python modulo 1
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

## Estruturas de condicionais
"""
print("\nEstruturas de condicionais")
saldo = 200
saque = 201

condição = 18
idade_usuario = 18

if condição > idade_usuario:
    print("Você não é maior de idade")
elif condição <= idade_usuario:
    print("Você é maior de idade idade")
    if saque > saldo:
        print("Você você não tem saldo suficiente")
    else:
        print("Saque realizado")
else:
    print("Não legivel")
    
### if ternario

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")



## Estruturas de repetições

print("\nEstruturas de repetições")

### For
print("For")

num = int(input("Digite um numero inteiro: "))
print(num)

frase = "Vamos lá"
for  letra in frase:
    print(letra, end = '-')

for  numm in range(num):
    print(numm)
    
for valor in range(0, 51, 5):
    print(valor)
    
### While
print("\nWhile")

opção = True
while opção:
    usuario = int(input("\nDgite um numero para saber se é par ou impar ou 0 para sair: "))
    resto = usuario % 2
    if resto == 0 and usuario != 0:
        print("Seu numero é par")
    elif resto > 0:
        print("Seu numero é impar")
    else:
        opção = False
else:
    print("Saindo")
    
## Manipulando Strings

print("\nManipulando Strings")

### Métodos
print("Métodos")
nome = "maTeuS"
curso = "  PYTHON "

print(nome.upper()) # Converte tudo em maiúsculo
print(nome.lower()) # Converte tudo em minúscula
print(nome.title()) # Converte tudo em título

print(curso.strip()) # Remove todos os espaços em brancos 
# Podendo utilizalo assim print(curso.strip() + ".") cmd>>> Python.
print(curso.lstrip()) # Remove os espaços em brancos da esquerda
print(curso.rstrip()) # Remove os espaços em brancos da direita

print(curso.center(20,"-")) # Centraliza por meio de caracteres (exemplo: --PYTHON--)
print(".".join(curso)) # Adiciona um caracter apos cada item

## Interpolação de variáreis 
print("\nInterpolação de variáreis")
### Utilizando %
print("Utilizando %")
nome = "Matheus"
idade = 19
profissao = "Programador"
linguagem = "Python"

print("Olá meu nome é %s tenho %d anos trabalho como %s utilizando %s." % (nome,idade,profissao,linguagem))

### Utilizando .format
print("\nUtilizando .format")
print("Opção 1")
print("Olá meu nome é {0} tenho {1} anos trabalho como {2} utilizando {3}." .format(nome,idade,profissao,linguagem))

print("\nOpção 2")
print("Olá meu nome é {nome} tenho {idade} anos trabalho como {profissao} utilizando {linguagem}." .format(nome=nome,idade=idade,profissao=profissao,linguagem=linguagem))

#print("\nOpção 3")
#print("Olá meu nome é {nome} tenho {idade} anos trabalho como {profissao} utilizando {linguagem}." .format(**pessoa))

### Utilizando f-string
print(f"Olá meu nome é {nome} tenho {idade} anos trabalho como {profissao} utilizando {linguagem}.")

PI = 3.14159
print(f"Valor de pi é {PI:.2f}") # Limita a quantidade de numeros após a virgula(pomto)
print(f"Valor de pi é {PI:10.2f}") # Adiciona espaçoes antes do valor da vareavel e limita a quantidade de numeros após a virgula(pomto)

