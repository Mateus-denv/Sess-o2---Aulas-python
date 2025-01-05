# Uma função que multiplica todos os argumentos não nomeados receidos. Retorne o total para um variável e mostre o valor da variável.
nmr = []
while True:
    def soma(*args):
        total = 0
        for numero in args:
            total += numero
        return total
    
    
    nmr_adc = int(input("Digite o numero para somar:"))
    
    nmr.append(nmr_adc)
    op = int(input("ADC MAIS UM NMR? S-1\nN-2:\n"))
    if op == 1:
        print(f"{nmr=}")
        continue
    elif op == 2:
        soma_total = soma(*nmr)
        print(F"{soma_total=}")
        break


# Um função para se saber se o numero é impar ou par


