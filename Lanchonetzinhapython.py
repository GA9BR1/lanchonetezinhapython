from time import sleep
produtos = {'nome100': 'Cachorro Quente', 'nome101': 'Bauru Simples', 'nome102': 'Bauru com Ovo',
            'nome103': 'Hamburguer', 'nome104': 'Cheeseburguer', 'nome105': 'Suco', 'nome106': 'Refrigerante'}
precos = {'preço100': 1.20, 'preço101': 1.30, 'preço102': 1.50, 'preço103': 1.20, 'preço104': 1.70, 'preço105': 2.20,
          'preço106': 1.00}

codigos = [100, 101, 102, 103, 104, 105, 106]

soma = 0
contar100 = 0
contar101 = 0
contar102 = 0
contar103 = 0
contar104 = 0
contar105 = 0
contar106 = 0

totcontar100 = 0
totcontar101 = 0
totcontar102 = 0
totcontar103 = 0
totcontar104 = 0
totcontar105 = 0
totcontar106 = 0


def menu():
    print('-'*50)
    print('Especificação         Código            Preço')
    print('-'*50)
    print(f'{produtos["nome100"]}        100', '           R$ 1.20')
    print(f'{produtos["nome101"]}          101', '           R$ 1.30')
    print(f'{produtos["nome102"]}          102', '           R$ 1.50')
    print(f'{produtos["nome103"]}             103', '           R$ 1.20')
    print(f'{produtos["nome104"]}          104', '           R$ 1.70')
    print(f'{produtos["nome105"]}                   105', '           R$ 2.20')
    print(f'{produtos["nome106"]}           106', '           R$ 1.00')
    print('-'*50)


while True:
    menu()
    sleep(0.5)
    codigo = int(input('Digite o código do produto: '))
    while codigo not in codigos:
        print('Código inexistente')
        codigo = int(input('Digite o código do produto: '))
    quant = int(input('Digite a quantidade do produto: '))
    if codigo == 100:
        soma = soma + (precos['preço100'] * quant)
        totcontar100 = totcontar100 + (precos['preço100'] * quant)
        contar100 = contar100 + (1 * quant)
        print('Produto adicionado com sucesso !')
        sleep(1.5)
    if codigo == 101:
        soma = soma + (precos['preço101'] * quant)
        totcontar101 = totcontar101 + (precos['preço101'] * quant)
        contar101 = contar101 + (1 * quant)
        print('Produto adicionado com sucesso !')
        sleep(1.5)
    if codigo == 102:
        soma = soma + (precos['preço102'] * quant)
        totcontar102 = totcontar102 + (precos['preço102'] * quant)
        contar102 = contar102 + (1 * quant)
        print('Produto adicionado com sucesso !')
        sleep(1.5)
    if codigo == 103:
        soma = soma + (precos['preço103'] * quant)
        totcontar103 = totcontar103 + (precos['preço103'] * quant)
        contar103 = contar103 + (1 * quant)
        print('Produto adicionado com sucesso !')
        sleep(1.5)
    if codigo == 104:
        soma = soma + (precos['preço104'] * quant)
        totcontar104 = totcontar104 + (precos['preço104'] * quant)
        contar104 = contar104 + (1 * quant)
        print('Produto adicionado com sucesso !')
        sleep(1.5)
    if codigo == 105:
        soma = soma + (precos['preço105'] * quant)
        totcontar105 = totcontar105 + (precos['preço105'] * quant)
        contar105 = contar105 + (1 * quant)
        print('Produto adicionado com sucesso !')
        sleep(1.5)
    if codigo == 106:
        soma = soma + (precos['preço106'] * quant)
        totcontar106 = totcontar106 + (precos['preço106'] * quant)
        contar106 = contar106 + (1 * quant)
        print('Produto adicionado com sucesso !')
        sleep(1.5)
    op = str(input('Quer continuar adicionando [S/N]? ')).upper().strip()[0]
    while op not in 'SsNn':
        print('Opção inválida !')
        op = str(input('Quer continuar adicionando [S/N]? ')).upper().strip()[0]
    if op in 'N':
        print(f'O resultado da conta foi de R${soma:.2f}')
        if contar100 > 1:
            print(f'{contar100:.0f}x {(produtos["nome100"])} = R${totcontar100:.2f}')
        if contar101 > 1:
            print(f'{contar101:.0f}x {(produtos["nome101"])} = R${totcontar101:.2f}')
        if contar102 > 1:
            print(f'{contar102:.0f}x {(produtos["nome102"])} = R${totcontar102:.2f}')
        if contar103 > 1:
            print(f'{contar103:.0f}x {(produtos["nome103"])} = R${totcontar103:.2f}')
        if contar104 > 1:
            print(f'{contar104:.0f}x {(produtos["nome104"])} = R${totcontar104:.2f}')
        if contar105 > 1:
            print(f'{contar105:.0f}x {(produtos["nome105"])} = R${totcontar105:.2f}')
        if contar106 > 1:
            print(f'{contar106:.0f}x {(produtos["nome106"])} = R${totcontar106:.2f}')
        break
    if op in 'S':
        continue
input()
