
def deposito(valor_deposito, saldo_conta, extrato_conta):
    if valor_deposito > 0:
        saldo_conta += valor_deposito
        extrato_conta += f'D + R${valor_deposito}\n'
        print(f'Saldo em conta: R${saldo_conta}')
    else:
        print('A quantia para depósito deve ser maior que zero.')
    return saldo_conta, extrato_conta
    
def saque(*, saldo_conta, num_saque, limite, extrato, limite_saques):
        if saldo_conta > 0 and limite_saques > num_saque:
            valor = int(input('Quanto deseja sacar? R$'))
            if valor <= limite:
                check_saldo = saldo_conta - valor
                if check_saldo >= 0:
                    saldo_conta -= valor
                    print(f'Saque realizado.')
                    num_saque += 1
                    extrato += f'S - R${valor}\n'
                    print(f'\n\nSaques realizados hoje: {num_saque}')
                else:
                    print(f'Saldo insuficiente.')
            else:
                print('Limite de saque excedido (R$500).')
        elif saldo_conta == 0:
            print('Sem saldo na conta.')
        else:
                print('Limite de saques atingido para o dia. Retorne amanhã ou fale com o gerente da sua conta.')
        return saldo_conta, num_saque, extrato


def extrato(saldo_conta, /, *,  extrato_conta):
    if not extrato_conta:
         print('Sem histórico de transações.')
    else:
         print(extrato_conta)
    print(f'Saldo: R${saldo_conta}')
    
    return saldo_conta, extrato_conta

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
    

def alterar_senha(banco_dados):
    insert_conta = int(input('conta: '))
    insert_nome = str(input('nome: ' )).strip()
    insert_cpf = int(input('Digite CPF: '))
    if insert_nome == banco_dados[insert_conta]['NOME'] and insert_cpf == banco_dados[insert_conta]['CPF']:
        while True:
            nova_senha = int(input('digite a nova senha: '))
            confirme_senha = int(input('digite a nova senha: '))
            if nova_senha == confirme_senha:
                banco_dados[insert_conta]['SENHA'] = nova_senha
                break
            else:
                print('Valores diferentes. Tente novamente.')
                continue
    else:
        print('Dados incorretos. Fim do programa')
    banco_dados = acesso(0, banco_dados)
    return banco_dados


def cadastro(agencia, num_conta, banco_dados):
    cpf = int(input('Digite o seu CPF (sem pontos e traço): '))
    nome = str(input('Digite o seu nome completo: ')).rstrip().lstrip().upper()
    usuario = verif_usuario(cpf, nome, banco_dados)

    if usuario:
         print('JÁ EXISTE UM OUTRO USUARIO COM ESTE MESMO CPF, TENTE NOVAMENTE OU CONVERSE COM O GERENTE.')
         cadastro(agencia=agencia, num_conta=num_conta, banco_dados=banco_dados)
    else:
        endereco = str(input('Digite o seu endereco (rua, num, bairro, cidade/uf): ')).upper()
        senha = int(input('Digite sua senha: '))
        num_conta += 1
        conta = {
            'AGENCIA' : agencia,
            'CONTA' : num_conta,
            'NOME' : nome,
            'CPF' : cpf,
            'ENDERECO' : endereco,
            'SENHA' : senha
        }
        banco_dados[num_conta]=conta
        print(f'Bem-vindo {nome}! Segue informações da sua conta:\n\nAgência: {agencia}\nC/C: {num_conta}')

    return num_conta, banco_dados

def verif_usuario(cpf, nome, banco_dados):
    usuario_encontrado = []
    for conta in banco_dados:
        for usuario in banco_dados[conta]:
            if cpf == banco_dados[conta]['CPF'] and nome != banco_dados[conta]['NOME']:
                 usuario_encontrado.append(usuario)
            else:
                 None
    return usuario_encontrado[0] if usuario_encontrado else None

def listar(*, banco_dados):
        lista = []
        lista.append(banco_dados)
        for conta in lista:
             for val in conta.values():
                  print('AGENCIA\tCONTA\tNOME')
                  print(f"{val['AGENCIA']}\t{val['CONTA']}\t{val['NOME']}")
        
     
def main():

    AGENCIA = "0001"
    num_conta = 0000
    banco_dados = {}
    home_page = '''

[A] ACESSAR CONTA (CLIENTES)
[C] CADASTRAR NOVA CONTA 
[L] LISTAR CONTAS

'''
    while True:

        opcao = str(input(home_page)).upper()

        if opcao == 'A':
            banco_dados = acesso(0, banco_dados)
            

        elif opcao == 'C':
            num_conta, banco_dados  = cadastro(agencia=AGENCIA, num_conta=num_conta, banco_dados=banco_dados)
            

        elif opcao == 'L':
            listar(banco_dados=banco_dados)



def menu(banco_dados, num_conta):
    import sys
    saldo = 0
    extrato_conta = ''
    numero_saques = 0
    LIMITE_SAQUES = 3
    LIMITE = 500
    print(f'==============BEM-VINDO {banco_dados[num_conta]["NOME"]}!===============') 

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
                    saldo, numero_saques, extrato_conta = saque(saldo_conta=saldo, num_saque=numero_saques, limite=LIMITE, extrato=extrato_conta, limite_saques=LIMITE_SAQUES)
                

            elif opcao == 'E':
                print('Extrato')
                saldo, extrato_conta = extrato(saldo, extrato_conta=extrato_conta)
 
            elif opcao == 'Q':
                print('Obrigado por usar nosso sistema. Tenha um bom dia!')
                sys.exit()

            else:
                print('Operacao inválida. Por favor selecione uma opção válida.')


main()
