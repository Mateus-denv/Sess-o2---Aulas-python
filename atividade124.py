respostas = None
def verificacao(resp): 
    for index, chave in enumerate(perguntas):
        if resp == chave['Resposta']:
            return True
    return False

def enviar_resposta(env):
    try:
        print(env)
        print(chave['Opções'][env])
        respostas = chave['Opções'][env]
    except IndexError:
        print("Opção invalida")

    verificacao(resp=respostas)
perguntas = [
    {
        'Pergunta':'Qual é o codigo?',
        'Opções': ['123','345','678',],
        'Resposta': '123'
    },
    {
        'Pergunta' : 'Qual o meu nome?',
        'Opções' : ['Matheus' , 'Lucas', 'Pedro'],
        'Resposta' : 'Matheus',
    },
    {
        'Pergunta' : 'Qual a sua idade?',
        'Opções' : ['12', '16' , '19'],
        'Resposta' : '19',
    },
]

for index, chave in enumerate(perguntas):
    print(perguntas[index]['Pergunta'])
    for index, chave_interna in enumerate(chave['Opções']):
        print(index,"-",chave_interna)
    esc_op = int(input("|>"))
    enviar_resposta(esc_op)
    
    
    # print("Parabens Você acertou" if condicao else "Você errou")
    # Parei onde esta dando erro no valor boleano