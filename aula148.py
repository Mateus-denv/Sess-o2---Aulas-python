# try e except, else e finally para tratar exceções
# a = 18
# b = 0
# c = a / b

"""try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')"""

# ATT1
# Objetivo: Peça para o usuário digitar um número. Converta-o para int e trate o erro caso ele digite algo inválido.
"""num = input("Digite um numero: ")
try:
    soma = num / 2
except TypeError:
    print("Este numero é uma STR")"""
    
    
# ATT2
# Objetivo: Solicite dois números e divida um pelo outro, tratando divisão por zero.

"""entrada = int(input("Digite um numero: "))
entrada2 = int(input("Digite outro numero: "))
try:
    divisao = entrada // entrada2
    print(divisao)
    divisao2 = entrada2 // entrada
    print(divisao)
except ZeroDivisionError:
    print("Não é possiviel dividisão por zero 0")"""
    
# ATT3
# Objetivo: Peça um índice e tente acessar esse índice em uma lista fixa.
nome = input('digite um nome: ')
print(f"Este nome é {nome} ")
try:
    print(f"A a primeria letra é {nome[0]}")
except IndexError:
    print("Este index não existe")
else:
    print("Ocorreu como deveria")
finally:
    print(f"O utimo digito é {nome[6]}")
    