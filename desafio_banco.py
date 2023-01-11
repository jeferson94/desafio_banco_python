menu = """

[D] DEPOSITAR
[S] SACAR
[E] EXTRATO
[Q] SAIR

"""
saldo = 0
LIMITE = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        print('Depósito')
        deposito = 0
        while  deposito <= 0:
            deposito = float(input('Quanto deseja depositar? '))
            if deposito > 0:
                extrato += f'D + R${deposito:.2f}\n'
                saldo  += deposito
                break
            else:
                print('A quantia para depósito deve ser maior que zero.')
    
    elif opcao == 's':
        print('Saque')
        while saldo > 0:
            if numero_saques < LIMITE_SAQUES:
                saque = float(input('Quanto deseja sacar? '))
                if saque <= LIMITE:
                    check_saldo = saldo - saque
                    if check_saldo < 0:
                        print('Saldo insuficiente. Insira um novo valor de saque.')
                        continue
                    else:
                        saldo -= saque
                        print('Saque realizado.')
                        numero_saques += 1
                        extrato += f'S - R${saque:.2f}\n'
                        break
                else:
                    print('Limite de saque excedido (R$500). Inisira novo valor.')
            
            if numero_saques == LIMITE_SAQUES:
                print('Limite de saques atingido para o dia. Retorne amanhã ou fale com o gerente da sua conta.')
                break
        if saldo == 0:
            print('Sem saldo na conta.')
            continue

    elif opcao == 'e':
        print('Extrato')
        print('Não foram realizadas transações.'if not extrato else extrato)
        print(f'Saldo: R${saldo:.2f}')

    elif opcao == 'q':
        print('Obrigado por usar nosso sistema. Tenha um bom dia!')
        break

    else:
        print('Operacao inválida. Por favor selecione uma opção válida.')