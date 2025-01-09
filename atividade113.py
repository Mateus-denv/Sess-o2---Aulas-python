# Uma função que multiplica todos os argumentos não nomeados receidos. Retorne o total para um variável e mostre o valor da variável.

import re
nmr = []
"""
while True:
    def soma(*args):
        total = 0
        for numero in args:
            total += numero
        return total
    
    entrada_user = input("Digite o numero para somar: ")
    nmr_adc = re.sub(r'[^0-9]','',entrada_user)
    if len(nmr_adc) == 0:
        print("Digite somente numeros inteiros")
        continue
    
    nmr.append(int(nmr_adc))
    print(nmr)
    op = int(input("ADC MAIS UM NMR? \nS-1\nN-2: "))
    if op == 1:
        continue
    elif op == 2:
        soma_total = soma(*nmr)
        print(F"Soma de todos os elmentos é {soma_total}.")
        print("\nPROGRAMA ENCERRADO\n")
        break
"""


# Um função para se saber se o numero é impar ou par
while True:
    def impar_par(numero):
        deicisao = numero % 2
        print(f"Este numero [{numero}] é par"if deicisao == 0 else "Este numero é impar")
        return
    
    entrada_user = input("Digite o numero para somar: ")
    nmr_user = re.sub(r'[^0-9]','',entrada_user)
    if len(nmr_user) == 0:
        print("Digite somente numeros inteiros")
        continue
    Numero = int(nmr_user)
    impar_par(Numero)
    break