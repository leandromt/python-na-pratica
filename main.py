import getpass
# os - utiliza alguns recursos do sistema operacional
import os


if os.name == 'nt':
    os_name = 'Windows'
    clear = lambda: os.system('cls')
else:
    os_name = 'Outros'
    clear = lambda: os.system('clear')

while True:
    clear()
    print("********************************************")
    print("************* CAIXA ELETRÔNICO *************")
    print("************ Sistema: {} **************".format(os_name))
    print("********************************************")

    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')
    #password_typed = input('Digite sua senha: ')

    account_lists = {
        '0001-02': {
            'agency': '0001-02',
            'password': '123123',
            'name': 'Fulano de Tal',
            'value': 123.23
        },
        '1234-01': {
            'agency': '0001-02',
            'password': '123123',
            'name': 'Fulano de Tal',
            'value': 500.20
        },
        '1234-02': {
            'agency': '0001-02',
            'password': '123123',
            'name': 'Fulano de Tal',
            'value': 652255.09
        },
    }

    # for i in account_lists:
        #print(i)

    print("")
    print("********************************************")
    print("************* CAIXA ELETRÔNICO *************")
    print("********************************************")
    if account_typed in account_lists and password_typed == account_lists[account_typed]['password']:
        clear()
        print('[1] - Ver saldo')
        print('[2] - Sair')
        option_type = input('Escolha uma opção acima: ')
        if option_type == '1':
            print('Seu saldo é: {:.2f}'.format(account_lists[account_typed]['value']))
        elif option_type == '2':
            break
        else:
            print('Opção Inválida!')
    else:
        print('Conta inválida!')

    print('')
    input('Precione <ENTER> para continuar...')

