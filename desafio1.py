# PROJETO DESAFIO DIO.ME 
# Criando um Sistema Bancário com Python

# O desafio proposto consistia na criação de um sistema bancário simples para um único usuário, respeitando quatro regras principais:
# - Não permitir depósitos ou saques com valores negativos;
# - Limitar saques a um valor máximo de R$ 500 por operação;
# - Restringir o número de saques a 10 por dia;
# - Registrar todas as movimentações em um extrato, acessível mediante solicitação do usuário.

from datetime import datetime, timedelta, timezone

menu = """
[D] depositar
[S] saldo
[C] sacar
[E] extrato
[Q] Sair

"""
LIMITES_DE_TRANSACOES_DIARIAS = 10
LIMITE_PARA_SAQUE = 500
trasacoes_realizadas = 0
extrato = []
saldo = 0

# Mascara no padrão brasileiro
mascara_ptbr = '%d/%m/%Y %H:%M'
# Data e hora atual SP
data_hora_atual = datetime.now(timezone(timedelta(hours=-3))).strftime(mascara_ptbr)

def vericar_limite():
    # Limite para de 1 dia para proximas 10 trasações
    LIMITE_DIARIO = 1
    
    # Data da renovação de limite
    data_limite = datetime.now(timezone(timedelta(hours=-3+LIMITE_DIARIO))).strftime(mascara_ptbr)
        
    validacao = data_hora_atual <= data_limite and trasacoes_realizadas <= LIMITES_DE_TRANSACOES_DIARIAS
    
    return validacao

def atualizar_extrato(tipo, valor):
    if tipo == "Deposito":
        
        data_deposito = datetime.now(timezone(timedelta(hours=-3))).strftime(mascara_ptbr)
        extrato.append(f"{tipo} R$ {valor:.2f} {data_deposito}")
        
    elif tipo == "Saque":
        
        data_saque = datetime.now(timezone(timedelta(hours=-3))).strftime(mascara_ptbr)
        extrato.append(f"{tipo} R$ -{valor:.2f} {data_saque}")
        
    else:
        print("Não foi possivel realizar transação")
   
def ver_saldo():
    print(f"Seu saldo atual é de R$ {saldo}")
    
def ver_extrato():
    print("Extrato".center(50,"-"))
    
    for chave in extrato:
        print(f"{chave}".center(50," "))
            
    print(f"Saldo total: {saldo:.2f}".center(50," "))

print(" BANCO PAN ".center(50,":"))
while True:
    
    opcao = input(menu).upper()
    
    if opcao == "D":# Depositar
        if vericar_limite() == True:
            
            entrada = float(input("Qual o valor do deposito:\n>>> "))
            
            if entrada > 0:
                saldo += entrada
                trasacoes_realizadas += 1
                atualizar_extrato("Deposito",entrada)
                print("Deposito realizado com sucesso")

            else:
                print("Não é possivel realizar transações abaixo de R$ 1,00")
        else:
            print(f"Você atingiu o limite diario\nNão é possivel realizar mais transações até {data_hora_atual}")
    
    elif opcao == "S":# Saldo
        print(f"Seu saldo atual é de R$ {saldo}")
        
    elif opcao == "C":# Sacar
        if LIMITES_DE_SAQUES != 0:
            sacar = float(input(f"Quanto deseja sacar?\n>>>"))
            
            if sacar < 500:
                
                if sacar > 0 and sacar < saldo:
                    extrato.update({f"Saque{LIMITES_DE_SAQUES}":f"R$ -{sacar}"})
                    LIMITES_DE_SAQUES -= 1
                    saldo -= sacar
                    print("Saques realizado com sucesso")
                else:
                    print(f"Você não possui saldo suficiente\nSaldo: R$ {saldo}")
                    
            else: 
                print("Não é possivel realizar saques acima de R$ 500")
        else:
            print(f"Não é possivel realizar mais saques\nLIMITE DE SAQUE DIARIO: {LIMITES_DE_SAQUES}")
            
    elif opcao == "E":# Extrato
        extrato.update({f"Saldo":f"R$ {saldo}"})
        print("Extrato".center(20,"-"))
        
        for chave in extrato.items():
            print(chave)
                      
    elif opcao == "Q":# Sair
        print("\nPrograma encerrado")
        break
    
    else:
        print("Opção invalida\n")