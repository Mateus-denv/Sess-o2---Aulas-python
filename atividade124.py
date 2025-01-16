respostas = None
def verificacao(resp): 
    for index, chave in enumerate(perguntas):
        if resp == chave['Resposta']:
            return 1
        

def enviar_resposta(env):
    try:
        respostas = chave['Opções'][env]
    except IndexError:
        print("Opção invalida")
        respostas = None
    return verificacao(resp=respostas)
    

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

acertos = 0
for index, chave in enumerate(perguntas):
    print(perguntas[index]['Pergunta'])
    for index, chave_interna in enumerate(chave['Opções']):
        print(index,"-",chave_interna)
    esc_op = int(input("Escolha uma Opção|>"))
    
    condicao = enviar_resposta(esc_op) == 1
    
    if condicao:
        print("Parabens Você acertou")
        acertos += 1
    else:
        print("Você errou")
        
print(f"Você acertou {acertos} de {3}")
    