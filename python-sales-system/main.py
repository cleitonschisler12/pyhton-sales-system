from estoque import *
from vendas import *
from utils import *

while True:
    linha()
    print('\033[31mMENU\033[m' .center(45))
    linha()
    cor('1 - ', 'Adicionar produto')
    cor('2 - ', 'Ver produtos')
    cor('3 - ', 'Vender produto')
    cor('4 - ', 'Ver total vendido')
    cor('5 - ', 'Sair')
    try:
        op = int(input('Digite o número da opção desejada:'))
    except:
        erro('Erro! opção inválida, tente novamente.')
        continue
    if op > 5 or op < 1:
        erro('Erro! opção inválida, tente novamente.')
        continue
    if op == 1:
        linha()
        print('\033[36mADICIONAR PRODUTOS\033[m' .center(45))
        linha()
        a = adicionar()
        if a == False:
            erro('Preço ou quantidade inválidas. tente novamente')
            continue
    if op == 2:
        ver()
    if op == 3:
        try:
            a = input('Nome do produto:').strip().upper()
            b = int(input('Quantidade vendida:'))
            c = venda(a,b)
            if c == False:
                continue
        except ValueError:
            erro('Erro tente novamente.')
            continue
    if op == 4:
        a = total_venda()
        if a == False:
            erro('Sem vendas computadas.')
            continue
    if op == 5:
        linha()
        print('\033[35mENCERRANDO O SISTEMA... VOLTE SEMPRE!\033[m')
        break