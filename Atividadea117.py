def duplica():
    def exibeD(numer):
        return numer*2
    return exibeD

nmr = input("Digite um numero: ")
valor = duplica()
print(valor(nmr))