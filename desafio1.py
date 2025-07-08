# Detalhes no arquivo nomeado desafio1.md

from datetime import datetime, timedelta, timezone

menu = """
[U] criar conta
[R] criar conta bancaria
[D] depositar
[S] saldo
[C] sacar
[E] extrato
[Q] Sair

"""
LIMITES_DE_TRANSACOES_DIARIAS = 10
LIMITE_PARA_SAQUE = 500
transacoes_realizadas = 0
extrato = []
saldo = 0
usuarios = [[0,1],[0,1],[0,1]]
contas = []
nome = ''
data_de_nascimento = ""
cpf = ''
endereco = ""
# Máscara para formatação de data e hora no padrão brasileiro
mascara_ptbr = '%d/%m/%Y %H:%M'
# Data e hora atual no fuso horário de São Paulo (GMT-3)
data_hora_atual = datetime.now(timezone(timedelta(hours=-3))).strftime(mascara_ptbr)


# Função para localizar o estado de cadastro
def localizar_estado():
    # loop incial para permite que usuario tente novamente
    while True: 
        estado = input("\nQual estado reside?\n>>> ")
        estado = estado.lower()  # padroniza para evitar erro com maiúsculas
        
        # Procura o estado informado e retorna sua sigla correspondente
        if estado == "acre":
            return "AC"
        elif estado == "alagoas":
            return "AL"
        elif estado == "amapa":
            return "AP"
        elif estado == "amazonas":
            return "AM"
        elif estado == "bahia":
            return "BA"
        elif estado == "ceara":
            return "CE"
        elif estado == "distrito federal":
            return "DF"
        elif estado == "espirito santo":
            return "ES"
        elif estado == "goias":
            return "GO"
        elif estado == "maranhao":
            return "MA"
        elif estado == "mato grosso":
            return "MT"
        elif estado == "mato grosso do sul":
            return "MS"
        elif estado == "minas gerais":
            return "MG"
        elif estado == "para":
            return "PA"
        elif estado == "paraiba":
            return "PB"
        elif estado == "parana":
            return "PR"
        elif estado == "pernambuco":
            return "PE"
        elif estado == "piaui":
            return "PI"
        elif estado == "rio de janeiro":
            return "RJ"
        elif estado == "rio grande do norte":
            return "RN"
        elif estado == "rio grande do sul":
            return "RS"
        elif estado == "rondonia":
            return "RO"
        elif estado == "roraima":
            return "RR"
        elif estado == "santa catarina":
            return "SC"
        elif estado == "sao paulo":
            return "SP"
        elif estado == "sergipe":
            return "SE"
        elif estado == "tocantins":
            return "TO"
        else:
            print("Estado não encontrado, certifique que estaja escrito da forma correta\n")
            
            
# Fução para indentificar se o usuario ja é cadastrado usando como verficação o CPF
def verificar_se_usuario_exite(usuario):
    cont = 0 # Zera o contador a cada verificação
    
    # loop para pegar cada cadastro
    for _cpf in usuarios:
        print(_cpf[0])
        
        # Se encotrado o cpf dentro da lista é comparado com o cpf recebido
        if _cpf[0] == usuario: 
            cont += 1  # Contador soma +1 e quebra o loop
            break
        
    # Se cont for zero, retorna (False) que significa que o usuario não existe
    validacao = cont is not 0 
           
    return  validacao

# Função onde é validade e verificado o cpf 
def validar_e_verificar_cpf():
    # Define uma mensagem de erro padrão para reutilizar em várias partes
    msg_erro = "Erro! Informe novamente, verifique se CPF o está escrito corretamente"

    # Laço infinito que só termina quando o CPF for válido e não estiver cadastrado
    while True:
        try:
            # Transforma em `int` para garantir que são apenas números, e depois de volta em `str`
            cpf = str(int(input("\nQual seu CPF?\nSem pontos(.) ou traço(-), somente numeros\n>>> ")))
            
            # Verifica se o CPF tem 11 dígitos
            if len(cpf) == 11:

                # Chama a função `verificar_se_usuario_exite` para ver se o CPF já está cadastrado
                if verificar_se_usuario_exite(cpf) == False:
                    # Se não estiver cadastrado, sai do loop
                    break
                else: 
                    # Se já estiver cadastrado, exibe mensagem de erro
                    print(f"Usuario ja cadastrado\n{msg_erro}")
                
            else:
                # Se o CPF não tiver 11 dígitos, exibe mensagem de erro
                print(msg_erro)
            
        except ValueError:
            # Caso o usuário digite algo que não seja número, mostra mensagem de erro
            print(msg_erro)
            
    # Retorna o CPF válido e não cadastrado
    return cpf
         
# Função para criar um usuario
def criar_usuario(_nome,_data_de_nascimento):
    
    # Chama a função que valida o CPF e garante que ele não está cadastrado
    cpf = validar_e_verificar_cpf()         
    
    logadoro = input("\nQual seu logadoro?\n(nome da rua, avenida, travessa etc)\n>>> ")
    bairro = input("\nQual seu bairro?\n>>> ")
    cidade = input("\nQual cidade reside?\n>>> ")
    
    # Chama a função que obtém a sigla do estado (SP, RJ, etc.)
    sigla_do_estado = localizar_estado()   

    # Monta o endereço completo com base nas informações anteriores
    endereco = f"{logadoro} - {bairro} - {cidade}/{sigla_do_estado}"
    
    # Adiciona os dados do novo usuário á `usuarios`
    usuarios.append([cpf, _nome, _data_de_nascimento, endereco])
    
    # Retorna uma mensagem informando que o usuário foi criado
    return "\nUsuario criado"

# Função para criar um conta
def criar_conta_bancaria():
    ...

# Função que verifica se o usuário ainda está dentro do limite diário de transações
def verificar_limite():
    # Define o limite de 1 dia (poderia ser mais elaborado com data de comparação real)        
    LIMITE_DIARIO = 1
    
    # Calcula o horário em que o limite diário teoricamente "renova"
    data_limite = datetime.now(timezone(timedelta(hours=-3+LIMITE_DIARIO))).strftime(mascara_ptbr)
    
    # Verifica se a data atual ainda está dentro do limite e se não excedeu o número de transações
    validacao = data_hora_atual <= data_limite and transacoes_realizadas <= LIMITES_DE_TRANSACOES_DIARIAS
    
    return validacao

# Função que atualiza o extrato com o tipo de transação (depósito ou saque) e valor
def atualizar_extrato(tipo, valor):
    
    # Obtém a data e hora atual no fuso horário de Brasília (UTC-3)
    # Em seguida, formata a data usando uma máscara personalizada (ex: "%d/%m/%Y %H:%M")
    data_hora_transação = datetime.now(timezone(timedelta(hours=-3))).strftime(mascara_ptbr)
    
    # Verifica se o tipo de operação é "Deposito"
    if tipo == "Deposito":
    
        # Adiciona ao extrato uma entrada com o tipo, valor formatado e a data
        extrato.append(f"{tipo} R$ {valor:.2f} {data_hora_transação}")
    
    # Verifica se o tipo de operação é "Saque"
    elif tipo == "Saque":
        
        # Adiciona ao extrato uma entrada com tipo, valor (negativo) e data
        extrato.append(f"{tipo} R$ -{valor:.2f} {data_hora_transação}")

    else:  # Fallback caso o tipo seja inválido
        print("Não foi possivel adicionar o valor no extrato")
    
# Função criada para realizar depósitos
def depositar(saldo, entrada, transacoes_realizadas):
    # Adiciona o valor da entrada ao saldo atual
    saldo += entrada

    # Incrementa o contador de transações realizadas
    transacoes_realizadas += 1

    # Atualiza o extrato com o tipo "Deposito" e o valor depositado
    atualizar_extrato("Deposito", entrada)

    # Retorna o saldo atualizado e o número de transações
    return saldo, transacoes_realizadas

# Função criada para realizar saques
def sacar(saldo, saida, transacoes_realizadas):
    # Subtrai o valor do saque do saldo atual
    saldo -= saida

    # Incrementa o contador de transações realizadas
    transacoes_realizadas += 1

    # Atualiza o extrato com o tipo "Saque" e o valor sacado
    atualizar_extrato("Saque", saida)

    # Retorna o saldo atualizado e o número de transações
    return saldo, transacoes_realizadas

# Função para exibir o saldo atual do usuário
def ver_saldo():
    print(f"Seu saldo atual é de R$ {saldo}")

# Função para exibir o extrato completo das transações
def ver_extrato():
    print("Extrato".center(50,"-"))
    
    for chave in extrato:
        print(f"{chave}".center(50," "))
            
    print(f"Saldo total: {saldo:.2f}".center(50," "))

print(" BANCO VILAVELHA ".center(50,":"))

# Loop principal do sistema bancário
while True:
    
    opcao = input(menu).upper() # Solicita a opção do usuário e converte para maiúsculo
    if opcao == "U": # Criar conta
        
        nome = input("Qual seu nome?\n>>> ")
        data_de_nascimento = input("\nQual sua data de nascimento?\nSiga esse padrão 11-11-2005\n>>> ")
        

        print(criar_usuario(nome,data_de_nascimento))
        
    elif opcao == "R": #Criar conta bancaria
        cpf_registrado = input("Digite cpf registrado\n>>> ")
    
    elif opcao == "D":# Depositar
        if verificar_limite() == True:
            
            entrada = float(input("Qual o valor do deposito:\n>>> "))
            
            if entrada > 0:
                saldo, transacoes_realizadas = depositar(saldo,entrada=entrada,transacoes_realizadas=transacoes_realizadas)
                print("Deposito realizado com sucesso")

            else:
                print("Não é possivel realizar transações abaixo de R$ 1,00")
        else:
            print(f"Você atingiu o limite diario\nNão é possivel realizar mais transações até {data_hora_atual}")
    
    elif opcao == "S":# Saldo
        ver_saldo()
        
    elif opcao == "C":# Sacar
        if verificar_limite() == True:
            valor = float(input(f"Quanto deseja sacar?\n>>> "))
            
            if valor < 500.00: # Atenção: valor limite é < 500, ou seja, R$ 499,99 é aceito, mas 500 não
                
                if valor > 0 and valor <= saldo:
                    saldo, transacoes_realizadas = sacar(saldo=saldo,saida=valor,transacoes_realizadas=transacoes_realizadas)
                    print("Saque realizado com sucesso")
                    
                else:
                    print(f"Você não possui saldo suficiente\nSaldo: R$ {saldo}")
                    
            else: 
                print("Não é possivel realizar saques acima de R$ 500")
                
        else:
            print(f"Você atingiu o limite diario\nNão é possivel realizar mais transações")
            
    elif opcao == "E":# Extrato
        ver_extrato()
                      
    elif opcao == "Q":# Sair
        print("\nPrograma encerrado")
        break
    
    else:
        print("Opção invalida\n")