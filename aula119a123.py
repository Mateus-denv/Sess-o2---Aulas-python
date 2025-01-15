pessoa = {

}

pessoa['Nome'] = 'Matheus'
pessoa['Codigo'] = [
    {'COD1': '123'},
    {'COD2': '456'},
]

#print(pessoa['Codigo'][0]['COD1'])

#del pessoa['Codigo'][0]['COD1']

#print(pessoa)

if  pessoa.get('Codigo') is None:
    print('NÃO EXISTE')
else:
    print('EXISTE')

pessoa.setdefault('Idade', 0)
# print(pessoa.__len__())
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
print(list(pessoa.items()))

for chave in pessoa.values():
    ...#print(chave)
    
print(pessoa.get('Nomt','Não existe'))

idade = pessoa.popitem()
print(idade)
print(pessoa)

pessoa.update(Nome='Lucas')
print(pessoa)
