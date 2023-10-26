user = input('Digite o usuario para cadastro: ')
password = input('Digite a senha para cadastro: ')

print("""
    Exames disponiveis:
    Exame A | 120 min | R$ 500
    Exame B | 60 min | R$ 300
""")

print("""
    Opções:
    1 - Agendar Exame
    2 - Remover um exame
    3 - Encerrar um exame
""")

totalTime = 0
totalCost = 0
quantity = 0

while True:
    opcao = int(input('Deseje a opção desejada: (1/2/3)'))
    if opcao == 1 or opcao == 2:
        exame = input('Qual exame você deseja realizar: ')

        if exame == "A":
            custo = 500
            tempo = 120
        elif exame == "B":
            custo = 300
            tempo = 60
        else:
            print('Escolha invalida!')

    if opcao == 1:
        if totalTime+tempo <= 8*60:
            totalTime += tempo
            totalCost += custo
            quantity += 1
            print('Exame adicionado com sucesso')
            print(f'O tempo total dos exames é {totalTime}')
        else:
            print('Não é possivel adicionar mais exames')
    elif opcao == 2:
        checkUser = input('Digite o usuario cadastrado: ')
        checkPassword = input('Digite a senha cadastrada: ')

        if checkUser == user and checkPassword == password:
            print('Usuario e senha validos, exame removido!')
            totalTime += tempo
            totalCost += custo
            quantity += 1
        else:
            print('Usuario e senha invalidos!')
    elif opcao == 3:
        print('Programa finalizado!')
        break
    else:
        print('Opção invalida')


print(f'O custo total dos exames é {totalCost}')
print(f'O tempo total dos exames é {totalTime}')
print(f'A quantidade total dos exames é {quantity}')
