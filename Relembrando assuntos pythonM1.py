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

## Fatiamento de strings
print("\nFatiamento de strings")

nome1 = "Python"
nome2 = "João Guilherme de Souza"

print(nome1[2]) # Pega um cacter
print(nome2[5:]) # Inicio
print(nome2[5:15]) # Inicio, fim 
print(nome2[5:15:5]) # Inicio, fim e pulando
print(nome2[::-1]) # Inverte a string

## String de múltiplas linhas
print("\nString de multiplas linhas")

nome = "Matheus"
mensaguem = f""Olá meu nome é {nome}
Estou no 3 semestre de TI""

print(mensaguem)

""" 
# Funções
"""print("\nFunções\n")

def exibir_mensagem():
    print("Olá mundo")
    
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo, {nome}")

def exibir_mensagem_3(nome="João"):
    print(f"Seja bem vindo, {nome}")

exibir_mensagem()
exibir_mensagem_2("Pedro")
exibir_mensagem_3()

    
def retorna_sucessor_e_antecesor(numero):
    antecessor = numero -1
    sucessor = numero +1
    return antecessor, sucessor

def calcuclar_total(numero):
    return sum(numero)

print(calcuclar_total([10,20,30]))
print(retorna_sucessor_e_antecesor(10))
print("\n")
def salva_moto (marca, ano, modelo, quilometragem):
    print(f'Moto adcionada\nModelo:{modelo}\nMarca:{marca}\nAno:{ano}\nQuilometragem:{quilometragem}')
    
print("SIMPLES")    
salva_moto("HONDA",2015,"CG125",1200.2)

print("\nNOMEADO")    
salva_moto(marca="HONDA", ano=2015, modelo="CG125", quilometragem=1200.2)

print("\nNOMEADO COMO DICIONARIO")    
salva_moto(**{"marca": "HONDA", "modelo":"CG125","ano": 2015, "quilometragem" : 1200.2})
"""

# *args trabalham com lista e tuplas
# **Kwargs trabalham com discionarios ou chave e valor

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
exibir_poema("Zen of python", "Beautigful is better than ugly",
             "Beautigful is better than ugly",
             "Beautigful is better than ugly",
             "Beautigful is better than ugly",
             "Beautigful is better than ugly",
             "Beautigful is better than ugly",
             "Beautigful is better than ugly",
             "Beautigful is better than ugly",
             "Beautigful is better than ugly",
             autor="Tim Peters", ano=1999)