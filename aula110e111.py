""" 
args - Argumentos não nomeados 
* - *args (enpacotamento e desempacotamento)
"""

x,y, *resto = 1,2,3,4
print(x, y, resto)

# def soma (x,y):
#    return x + y

def soma(*args): # Usado para passar um quantidade ilimitadas de argumentos
    total = 0
    for numero in args:
        total+=numero
    return total

numeros = 1,2,3  
soma_numeros = soma(*numeros)
print(soma_numeros)

print(sum(1,2,3))