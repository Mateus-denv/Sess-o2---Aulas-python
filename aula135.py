# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome' : 'Souza',
}

(a1, a2), (b1, b2) = pessoa.items()
#print(a1,a2)
#print(b2,b2)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}

# print(pessoa_completa)

# Kwargs - Keyword argumentos(argumentos nomeados)

def mostro_argumentos_nomeado(*args, **kwargs):
    print(args,"\n",kwargs)
    
mostro_argumentos_nomeado(1,2,3,nome='Matheus', qlq=123)

mostro_argumentos_nomeado(**pessoa_completa)