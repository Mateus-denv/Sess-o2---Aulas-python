def executa(funcao, *args):
    return funcao(*args)

"""def soma(x, y):
    return x + y

def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return multiplica"""
um = 1
dois = 2

duplica = executa(
    lambda m: lambda n: n * m, dois
)

print(duplica(2))

print(
    executa(
        lambda x, y: x + y, 
        um,dois
    ),
)

# duplica = criar_multiplicador(2)

