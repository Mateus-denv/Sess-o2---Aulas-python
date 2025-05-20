# Introdução ás generetor funcitions em python
# generator = (n for  nin range(1000000))

"""def gerenetor (n=0):
    return"""
def gerenetor (n=0):
    yield 1
    print("Continuando....")
    yield 2
    print("Continuando....")
    yield 3
    print("Vou termina....")
    return 'ACABOU'

gen = gerenetor(n=0)
print(next(gen))
print(next(gen))
print(next(gen))

"""

## ⚙️ Introdução às Generator Functions em Python

### ✅ O que são?

**Generator functions** são funções especiais em Python que **geram valores um de cada vez**, pausando a execução entre cada valor com a palavra-chave `yield`.

Elas **não retornam todos os valores de uma vez como uma lista**, mas sim um **objeto iterável (um generator)** que **produz os valores sob demanda** (lazy evaluation).

---

### 🧠 Por que usar generator functions?

* 🔁 **Economia de memória**: úteis para trabalhar com grandes volumes de dados.
* ⏩ **Mais eficientes**: não precisam calcular tudo de uma vez.
* 📦 **Facilitam a criação de iteradores personalizados**.

---

### 📌 Exemplo básico

python"""
def contador():
    for i in range(3):
        yield i

gen = contador()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
"""
# next(gen) agora daria StopIteration
```

---

### ⚡ Comparando com listas

```python
# Lista: consome memória imediatamente
lista = [i for i in range(1000000)]

# Generator: cria valores sob demanda
gen = (i for i in range(1000000))
```

O generator acima só calcula cada `i` **quando necessário**, economizando memória.

---

### 📦 Exemplo prático: Processar arquivos linha por linha

```python
"""
def ler_linhas_arquivo(caminho):
    with open(caminho, "r") as f:
        for linha in f:
            yield linha.strip()

for linha in ler_linhas_arquivo("dados.txt"):
    print(linha)
"""
```

🧠 Isso evita carregar todo o arquivo na memória — essencial para arquivos grandes.

---

### 🛠️ Quando usar generator functions?

Use quando:

* Precisa de **eficiência de memória**.
* Vai trabalhar com **fluxos contínuos de dados** (como sensores, streams ou arquivos grandes).
* Precisa criar seu próprio **iterador customizado**.

---

### 🚀 Resumo

| Função comum            | Generator Function      |
| ----------------------- | ----------------------- |
| Usa `return`            | Usa `yield`             |
| Executa tudo de uma vez | Executa passo a passo   |
| Retorna valor final     | Retorna uma sequência   |
| Consome mais memória    | Usa memória sob demanda |

"""