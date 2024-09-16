menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3

while(True):
    
    opcao = input(menu)

    match(opcao):
        case 'd':
            valor = float(input('informe o valor do deposito: '))
            if(valor > 0):
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor informado é inválido.")     
        case 's':
            valor = float(input('Informe o valor do saque: '))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques > LIMITE_SAQUES

            if(excedeu_limite):
                print("Operação falhou! O valor excede o limite.")
            elif(excedeu_saldo):
                print("Operação falhou! Você não tem saldo o suficiente.")
            elif(excedeu_saques):
                print("Operação falhou! Número maximo de saques excedido.")
            elif(valor > 0):
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Valor inserido é inválido.")
        case 'e':
            print(extrato)
        case 'q':
            print("saindo...")
            break
        case _:
            print("Opção invalida!")