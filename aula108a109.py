""" 
Escopo de funções em python 
Escopo significa o local onde aquele codigo pode atingir
Existe o escopo global e local.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados
"""
x = 1
y = 2

def escopo():
    def outro_escopo():
        global y
        y = 10
        print(f"{y=}")
    outro_escopo()
    print(f"{x=}")
        
print(f"{x=}{y=}")
escopo()