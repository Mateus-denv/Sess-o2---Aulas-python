class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []


    # TODOS: Implementar o método adicionar_venda para adicionar uma venda à lista de vendas:
    def adicionar_venda(self, venda):
        if isinstance(venda, Venda):
            vendas_feitas = venda.quantidade * venda.valor
            self.vendas.append(vendas_feitas)
        else:
            print("Não pertence a instancia")
    
    
    def calcular_total_vendas(self):
        total = 0
        print(self.vendas)
        for vendas in self.vendas:
                total += vendas
        return total
    # TODOS: Implementar o método total_vendas para calcular e retornar o total das vendas
        #return total

categorias = []

for i in range(1):
    nome_categoria = input("C: ")
    categoria = Categoria(nome_categoria)

    for j in range(2): 
        entrada_venda = input("QV: ") # Recebe em conjunto
        produto, quantidade, valor = entrada_venda.split(',') # adcionar separando por virgula
        
        quantidade = int(quantidade.strip())
        valor = float(valor.strip())
        print(produto,quantidade,valor) 

        venda = Venda(produto.strip(), quantidade, valor)
        
        # TODOS: Adicione a venda à categoria usando o método adicionar_venda:
        categoria.adicionar_venda(venda)

    categorias.append([categoria.nome,categoria.calcular_total_vendas()])

# Exibindo os totais de vendas para cada categoria
for index, categoriaa in enumerate(categorias):
    print(f"Vendas em {categoriaa[index]}: {categoriaa[index+1]}")
    
    
    # Eletrônicos
# Celular, 5, 1000
# Fone de Ouvido, 10, 500

# Vendas em Eletrônicos: 1500.0

    # Móveis
# Mesa, 2, 800
# Cadeira, 4, 400
	
# Vendas em Móveis: 1200.0

    # Alimentos
# Arroz, 10, 200
# Feijão, 7, 140

# Vendas em Alimentos: 340.0

    # Jardinagem
# Planta, 2, 60
# Ferramentas, 1, 100	

# Vendas em Jardinagem: 160.0

    # Livros
# Aventuras no Tempo, 1, 80
# Mistérios do Oceano, 2, 90

# Vendas em Livros: 170.0

    # Esportes
# Tênis, 7, 210
# Bola, 3, 120	

# Vendas em Esportes: 330.0