# Generator expression, iterables e iterators em python

iterable = ['eu', 'tenho', '__iter__']
iterator = iter(iterable) # __iter__ e __next__
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

generator = [n for n in range(1000)] # o generator é uma função que pausa e salva um valor por vez aa memoria mas não tem tamanho, não tem indice ao contrario do interable que trabalho com interalvel.
print(generator)

