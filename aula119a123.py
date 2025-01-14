pessoa = {

}

pessoa['nome'] = 'Matheus'
pessoa['Codigo'] = [
    {'COD1': '123'},
    {'COD2': '456'},
]

print(pessoa['Codigo'][0]['COD1'])

del pessoa['Codigo'][0]['COD1']

print(pessoa)

if  pessoa.get('Codigo') is None:
    print('NÃO EXISTE')
else:
    print('EXISTE')
