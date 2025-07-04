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
        entrada = int(input("Qual o valor do deposito:\n>>>"))
        if entrada > 0:
            cont += 1
            saldo += entrada
            extrato.update({f"Entrada{cont}":entrada})
        else:
            print("Não foi possivel realizar o deposito")
                
    elif opcao == "S":# Saldo
        print(f"Seu saldo atual é de {saldo}")
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
        ...
    else:
        print("N")