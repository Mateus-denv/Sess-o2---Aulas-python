# INTRODUÇÃO A FUNÇÕES
somas = 0
def soma(a, b, c=None):
    if c is not None:
        print(a+b+c)
    else:
        print(a+b)

print("Digite um valor pra soma:", end="")
numero = int(input(""))
soma(a=numero, b=2)