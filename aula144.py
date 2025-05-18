# Dir,hasattr, e getattr em python
# Verifica se existe o metodo ou não
string = 'Luiz'
print(string)

if hasattr(string, 'upper'):
    print("Existe upper")
    print(string.upper())