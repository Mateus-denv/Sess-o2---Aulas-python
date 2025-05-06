# Dictionary Comprehension e set Comprehension

produto = {
    "NUMERO" : 'caneta',
    'Preco' : 2.5,
    'Categoria': "Escritorio",
}

dc = {
    chave: valor.upper()
    if isinstance(valor,str) else valor
    for chave, valor
    in produto.items()
}

print(dc)

"""
No cotidiano da programação em Python, especialmente em tarefas de manipulação de dados, automação ou análise, o **Dictionary Comprehension** e o **Set Comprehension** são usados para escrever código mais limpo, rápido e expressivo. Aqui estão exemplos práticos de cada um:
"""

# Dictionary Comprehension – Prática cotidiana**

# Cria dicionários de forma concisa.

#### Exemplo 1: Mapeando produtos com desconto

precos = {"camisa": 50, "calça": 100, "sapato": 150}
desconto = 0.10

precos_com_desconto = {produto: preco * (1 - desconto) for produto, preco in precos.items()}
# {'camisa': 45.0, 'calça': 90.0, 'sapato': 135.0}

#### Exemplo 2: Filtrar apenas itens acima de um valor

precos_filtrados = {produto: preco for produto, preco in precos.items() if preco > 80}
# {'calça': 100, 'sapato': 150}

"""
Uso comum:

Gerar relatórios.
Transformar dados de APIs/planilhas.
Aplicar regras de negócio automaticamente.
"""
### Set Comprehension – Prática cotidiana

# Cria conjuntos eliminando duplicatas automaticamente.

# Exemplo 1: Obter tipos únicos de produtos em estoque

produtos = ["camisa", "calça", "camisa", "sapato", "sapato", "boné"]
tipos_unicos = {produto for produto in produtos}
# {'camisa', 'calça', 'boné', 'sapato'}

#### Exemplo 2: Palavras únicas de uma frase

frase = "a inteligência artificial é o futuro da inteligência"
palavras_unicas = {palavra for palavra in frase.split()}
"""
# {'é', 'inteligência', 'a', 'futuro', 'artificial','da'}

#### Uso comum:

Eliminar duplicatas.
Obter dados únicos de listas grandes.
Checagem de interseções, diferenças entre conjuntos.

#Quando usar cada um:

* Use *dictionary comprehension* quando você precisa de **pares chave: valor** com alguma lógica aplicada.
* Use **set comprehension** quando você precisa de uma **coleção única de elementos**, sem se importar com a ordem ou duplicação.

"""