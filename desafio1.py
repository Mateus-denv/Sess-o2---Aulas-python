menu = """
[D] depositar
[S] saldo
[C] sacar
[E] extrato
[Q] Sair

"""
saldo = 0
limite_para_saque = 500
extrato = {}
numero_de_saques = 0
LIMITES_DE_SAQUES = 3
       
        
while True:
    print("BANCO PAN")
    cont = 0
    opcao = input(menu).upper()
    
    if opcao == "D":# Depositar
    elif opcao == "S":# Saldo
        print(f"Seu saldo atual é de {saldo}")
    elif opcao == "C":# Sacar
        sacar = input(f"Quanto deseja sacar?\n>>>")
    elif opcao == "E":# Extrato
        ...
    elif opcao == "Q":# Sair
        ...
    else:
        print("N")