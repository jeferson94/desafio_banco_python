
def deposito(a,b,c):
    if a > 0:
        b += a
        c += f'D + R${a}\n'
        print(f'Saldo em conta: R${b}')
    else:
        print('A quantia para depósito deve ser maior que zero.')
    return b,c
    
def saque(a, b, c, d, e, f):
        if b > 0 and f > c:
            a = int(input('Quanto deseja sacar? R$'))
            if a <= d:
                check_saldo = b - a
                if check_saldo > 0:
                    b -= a
                    print(f'Saque realizado.')
                    c += 1
                    e += f'S - R${a}\n'
                    print(c)
                else:
                    print(f'Saldo insuficiente.')
            else:
                print('Limite de saque excedido (R$500).')
        elif b == 0:
            print('Sem saldo na conta.')
        else:
                print('Limite de saques atingido para o dia. Retorne amanhã ou fale com o gerente da sua conta.')
        return a, b, c, e

def extrato(a, b):
    print('Não foram realizadas transações.'if not b else b)
    print(f'Saldo: R${a:.2f}')
    
    return a, b

def acesso(tentativa, banco_dados):
    while tentativa < 3:
        insert_conta = int(input('conta: '))
        insert_senha = int(input('senha: '))
        if insert_conta not in banco_dados:
            print('conta nao cadastrada, tente novamente.')
            main()
        else:
            if insert_senha == banco_dados[insert_conta]['SENHA']:
                menu(banco_dados, insert_conta)
            else:
                print('Senha incorreta. Tente novamente.')
                tentativa += 1
                continue
    if tentativa > 2:
            print('senha bloqueada, altere a senha.')
            banco_dados = alterar_senha(banco_dados)

    return banco_dados
    

def alterar_senha(a):
    insert_conta = int(input('conta: '))
    insert_nome = str(input('nome: ' )).strip()
    insert_cpf = int(input('Digite CPF: '))
    if insert_nome == a[insert_conta]['NOME'] and insert_cpf == a[insert_conta]['CPF']:
        while True:
            nova_senha = int(input('digite a nova senha: '))
            confirme_senha = int(input('digite a nova senha: '))
            if nova_senha == confirme_senha:
                a[insert_conta]['SENHA'] = nova_senha
                break
            else:
                print('Valores diferentes. Tente novamente.')
                continue
    else:
        print('Dados incorretos. Fim do programa')
    a = acesso(0, a)
    return a

def cadastro(agencia, num_conta, banco_dados):
    nome = str(input('Digite o seu nome completo: ')).rstrip().lstrip().upper()
    cpf = int(input('Digite o seu CPF (sem pontos e traço): '))
    endereco = str(input('Digite o seu endereco (rua, num, bairro, cidade/uf): ')).upper()
    senha = int(input('Digite sua senha: '))
    num_conta += 1
    conta = {
        'NOME' : nome,
        'CPF' : cpf,
        'ENDERECO' : endereco,
        'SENHA' : senha
    }
    banco_dados[num_conta]=conta
    print(f'Bem-vindo {nome}! Segue informações da sua conta:\n\nAgêngia: {agencia}\nC/C: {num_conta}')
    print(banco_dados)

    return num_conta, banco_dados

def main():

    AGENCIA = 1
    conta = 0000
    bd_agencia = {}
    home_page = '''

[A] ACESSAR CONTA (CLIENTES)
[C] CADASTRAR NOVA CONTA 
[L] LISTAR CONTAS

'''
    while True:

        opcao = str(input(home_page)).upper()

        if opcao == 'A':
            bd_agencia = acesso(0, bd_agencia)
            

        elif opcao == 'C':
            conta, bd_agencia = cadastro(agencia=AGENCIA, num_conta=conta, banco_dados=bd_agencia)
            

        elif opcao == 'L':
            print(bd_agencia)


def menu(banco_dados, num_conta):

    saldo = 0
    extrato_conta = ''
    numero_saques = 0
    LIMITE_SAQUES = 3
    LIMITE = 500
    valor_saque = 0
    print(F'==============BEM-VINDO {banco_dados[num_conta]['NOME']}!===============')
    main_menu = """

    [D] DEPOSITAR
    [S] SACAR
    [E] EXTRATO
    [Q] SAIR

    """
        
    while True:

            opcao = input(main_menu).upper()

            if opcao == 'D':
                print('Depósito')
                valor_deposito = int(input('Quanto deseja depositar? R$'))
                saldo, extrato_conta = deposito(valor_deposito, saldo, extrato_conta)


            elif opcao == 'S':
                    valor_saque, saldo, numero_saques, extrato_conta = saque(a=valor_saque, b=saldo, c=numero_saques, d=LIMITE, e=extrato_conta, f=LIMITE_SAQUES)
                

            elif opcao == 'E':
                print('Extrato')
                saldo, extrato_conta = extrato(saldo, extrato_conta)

            elif opcao == 'Q':
                print('Obrigado por usar nosso sistema. Tenha um bom dia!')
                break

            else:
                print('Operacao inválida. Por favor selecione uma opção válida.')


main()
