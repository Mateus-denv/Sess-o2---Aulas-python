# Isinstace - para saber se objeto é de determinadado tipo

lista = [ 
         'a',1,1.1, True, [0,1,2], (1,2), {0,1},{ 'nome' : 'joao'}
]

for item in lista:
    if isinstance(item, set):
        print("SET")
        item.add(5)
        print(item, isinstance(item, set))
        
    elif isinstance(item, str):
        print("STR")
        print(item.upper())
        
    elif isinstance(item, (int, float)):
        print("NUM")
        print(item, item * 2 ) 
    else:
        print('Outro')
        
# Verifica se um objeto é de um tipo específico (ou de uma tupla de tipos):

isinstance(10, int)         # True
isinstance("abc", str)      # True
isinstance(3.14, (int, float))  # True

# Imagine uma função que calcula desconto. Você quer garantir que o valor seja numérico:

def aplicar_desconto(valor, desconto):
    if not isinstance(valor, (int, float)):
        raise ValueError("Valor deve ser numérico")
    return valor * (1 - desconto)

aplicar_desconto(100, 0.1)  # OK
aplicar_desconto("cem", 0.1)  # Levanta erro

dados = {"nome": "João", "idade": "30"}

"Tratamento de dados em APIs ou banco de dados \
 Muitas vezes você não sabe o tipo dos dados que chegam:"
if isinstance(dados["idade"], str):
    dados["idade"] = int(dados["idade"])
    
"""
isinstance() protege seu código contra erros por tipos inesperados. É essencial em:

Validações de entrada de usuário/API.

Filtragem de listas com múltiplos tipos.

Código robusto em sistemas de grande escala.

"""