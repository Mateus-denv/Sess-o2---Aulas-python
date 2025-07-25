# Relenbrando assuntos python modulo 2

## Listas
"""print("\nListas\n")

frutas = ["Laranja","Maçã"]

frutas = []

letras = list("Python")

print(frutas)
print(letras)

matriz = [
    [1, "a", 2],
    ["8", "d", 6],
    [4, "y", "c"]
    ]

print (matriz[0])
print (matriz[1][0])

lista = ["p","y","t","h","o","n"]

print(lista[2:])
print(lista[:2])
print(lista[2:1])
print(lista[1:1:1])
print(lista[::-1])

carro = ["gol", "cruze", "argo"]
for indice, modelo in enumerate(carro):
    print(f"{indice}: {modelo}")
    
### Filtro de verção
print("\nFiltro de verção\n")

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

### Compreenção de listas
print("\nCompreenção de listas\n")

pares_ = [numero for numero in numeros if numero % 2 == 0]
print(pares_)

numeros_2x = [numero ** 2 for numero in numeros ]
print(numeros_2x)

lista_8 = [(n**2 if n > 6 else n) for n in range(10) if n % 2 == 0] 
print(lista_8)
"""
## Metodos da classes list
"""print("\nMetodos da classes list")

print("\nAPPEND")
lista_1 = []
lista_1.append("Oi")
lista_1.append(1.5)
lista_1.append([10,12,20])
print(lista_1)


print("\nCOPY E CLEAR")
lista_2 = lista_1.copy()
lista_1.clear()
print(lista_1)
print(lista_2)

print("\nCOUNT")
print(lista_2.count(1.5)) # Conta quantas vezes o elemento aparece na lista

print("\nEXTEND")
lista_3 = ["20",25]
lista_3.extend(lista_2)
print(lista_3)

print("\nINDEX")
print(lista_3.index("Oi"))

print("\nPOP")
lista_3.pop(3)
print(lista_3)

print("\nREMOVE")
lista_3.remove("Oi")
print(lista_3)

print("\nREVERSE")
lista_3.reverse()
print(lista_3)

print("\nSORT ORDEM A-Z")
lista_4 = ["ANA", "JULIA", "BIA", "LORENA", "MATEUS", "HENRRIQUE"]
lista_4.sort()
print(lista_4)

print("\nSORT ORDEM Z-A")
lista_4.sort(reverse=True)
print(lista_4)

print("\nSORT ORDEM POR TAMANHO .len()")
lista_4.sort(key=lambda x: len(x))
print(lista_4)

print("\nSORT ORDEM POR TAMANHO .len() reverse")
lista_4.sort(key=lambda x: len(x), reverse=True)
print(lista_4)

print("\n.len()")
print(len(lista_4))

print("\nSORTED A-Z")
print(sorted(lista_4))

print("\nSORTED .len()")
print(sorted(lista_4,key=lambda x: len(x) ))

print("\nSORTED .len() reverse")
print(sorted(lista_4,key=lambda x: len(x), reverse=True))

## tuplas
print("\ntuplas\n")

nomes = ("ANA", "JULIA", "BIA", "LORENA", "MATEUS", "HENRRIQUE",)
print(nomes[2])
print(nomes[-4])

matriz_tupla = (
    (1,2,3),
    (3,4,5),
    (4,5,6)
)
print(matriz_tupla[2][1])

tupla = ("p","y","t","h","o","n")

print(tupla[:4])
print(tupla[::-1])

## Metodos da classes tuplas
print("\nMetodos da classes tuplas")

print(tupla.count)
print(nomes.index("ANA"))
print(len(tupla))
"""
## Estruturas de dados sets {}
"""print("\nEstruturas de dados\n")

print(set([1,2,3,4,5,5]))
print(set("abacaxi"))

liguagens = set(("Python", "Java", "Python"))
print(liguagens)

carros = {"uno", "gol", "fiat", "gol"}
print(set(carros))

### Acessando valores
print("\nAcessando valores")

numeros = {1,2,3,4}
print(numeros)

for index, carro in enumerate(carros):
    print(f"{index}: {carro}")
    
### Union
print("\nunion")
conjunto_a = {1,2}
conjunto_b = {1,2,3,4,5}
print(conjunto_a.union(conjunto_b))

### intersection -> remove os iguais
print("\nintersection")
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
print(conjunto_a.intersection(conjunto_b))

### difference -> remove os diferentes
print("\ndifference")
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
print(conjunto_a.difference(conjunto_b))

### Symmetric_difference -> os elementos que não são iguais
print("\nsymmetric_difference")
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
print(conjunto_a.symmetric_difference(conjunto_b))

### issubset -> Se dentro de um conjunto a outro por inteiro ou seja se todos os elementos que estão no A tambem estão em B
print("\nissubset")
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

### isdisjoint -> Se não a nenhum elemento igual nos conjunto nenhum conjunto 
print("\nisdisjoint")
conjunto_a = {10,22,44}
conjunto_b = {1,2,3,4,5}
conjunto_c = {7,8,9,10}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

### .add -> Se não existir ele é adcionado
print("\n.add")
sorteio_a = {10,22,44}

sorteio_a.add(1)
sorteio_a.add(12)

print(sorteio_a)

### .clear -> limpar
print("\n.add")
sorteio_a = {10,22,44}

sorteio_a.clear()
print(sorteio_a)

### .copy -> cria ma copia
print("\n.copy")
sorteio_a = {10,22,44}

sorteio_b = sorteio_a.copy()
print(sorteio_b)

### .discard -> descarta um elemento
print("\n.discard")
sorteio_a = {10,22,44}

sorteio_a.discard(10)
print(sorteio_a)

### .pop -> retira sempre o valor da frente
print("\n.pop")
sorteio_a = {5,9,10,22,44}

sorteio_a.pop()
print(sorteio_a)

### .remove -> remove recebendo um valor se o valor existir
print("\n.remove")
sorteio_a = {5,9,10,22,44}

sorteio_a.remove(9)
print(sorteio_a)

### .len
print("\n.len")
sorteio_a = {5,9,10,22,44}

print(len(sorteio_a))

### in -> verificar se o elemento existe no conjunto
print("\nin")
sorteio_a = {5,9,10,22,44}

print(1 in(sorteio_a))
"""
## Dicionarios: Criação e acesso aos dados

"""pessoa = {"nome":"guilherme", "idade": 28}

pessoa = dict(nome ="guilherme", idade =28)

print(pessoa)
pessoa["telefone"] = "74-658-654-211"

print(pessoa["telefone"])

dicionario = {
    "joao": {"idade": 12, "possue": True},
    "pedro": {"idade": 15, "possue": True},
    "guilherme": {"idade": 18, "possue": True}
}

print(dicionario["guilherme"]["idade"])
print("\n")
for chave,valor  in dicionario.items():
    print(f"{chave}:{valor}")
    
## Metodos class dict
print("\nMetodos class dict\n")

print("\nCopy\n")
dicionario_2 = dicionario.copy()
print(dicionario_2)

print("Clear")
dicionario.clear()
print(dicionario)

print("\n.fromkeys\n")
teste = {}
print(teste.fromkeys(["nome","telefone"]))
print(teste.fromkeys(["nome","telefone"],"vazio"))

## get
print("\n.get")

print(pessoa.get("v", {})) # Se não encontra retorna algo

### items
print("\n.items")
print(pessoa.items())

### keys
print("\n.keys")
print(pessoa.keys())

### pop
print("\n.pop")
print(pessoa.pop("nome"), {})
print(pessoa)

### popintem
print("\n.popintem")
print(pessoa.popitem())
print(pessoa)

### sefdefault
print("\n.setdefault")
print(pessoa.setdefault("nome","julia"))
print(pessoa)

### Update
print("\n.update")
pessoa.update(dicionario_2)
print(pessoa)

### Values
print("\n.Values")
print(pessoa.values())

### in
print("\n in")
resultado = "nome" in pessoa
print(resultado)

### del
print("\n.del")
del pessoa["nome"]
print(pessoa)
"""

## Trabalhando com objetos date, datetime e time

"""from datetime import date,datetime, time
data = date(2023,7,19).today()
print(data)

data_hora = datetime(11,11,11,).today()
print(data_hora)

hora = time(10,20,0)
print(hora)
"""
## Manipulando datas com timedelta
"""import datetime

d = datetime.datetime(2025,7,2,14,50)
d = d + datetime.timedelta(weeks=1)
print(d)"""

### Montando exemplo
"""
from datetime import date, datetime, timedelta, time

tipo_carro = ''
tempo_pequeno  = 100
tempo_medio = 200
tempo_grande = 1000
data_atual = datetime.now()

if tipo_carro == 'p':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"Data prevista é {data_estimada}")
    
elif tipo_carro == 'm':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"Data prevista é {data_estimada}")

else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"Data prevista é {data_estimada}")
    
    
### Mostrando somente o prazo com dias
print(date.today() - timedelta(days=1))

### Mostrando somente o prazo com horas
resultado = datetime(2025,7,5,10,30,0) - timedelta(hours=1)
print(resultado.time())

### Mostrando somente a data atual sem prazos

print(datetime.now().date())
"""
### Formatando e convertendo datas com strftime e strptime

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_string = "2025-07-08 10:20"

### Formando a data e hora
mascara_ptbr = '%d/%m/%Y %a'
mascara_enusa = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr)) # strftime serve para converter

print(datetime.strptime(data_hora_string, mascara_enusa))

### Trabanhando com timezone

"""#### utilizando o pytz
import datetime
import pytz

from datetime import datetime

data = datetime.now(pytz.timezone('Europe/Oslo'))
data2 = datetime.now(pytz.timezone('America/Sao_Paulo'))

print(data)
print(data2)"""

#### Utilizando o timezone
"""
from datetime import datetime, timedelta, timezone

data_os = datetime.now(timezone(timedelta(hours=2))) # Oslo
data_sp = datetime.now(timezone(timedelta(hours=-3))) # São Paulo

print(data_os)
print(data_sp)"""