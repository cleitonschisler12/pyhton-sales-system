from utils import *

prod = []
produtos = {}
produto = {}

def lista(produtos):
    prod.append(produtos)

def adicionar():
    nome = input('Nome do produto:').strip().upper()
    try:
        preco = float(input('Valor do produto:'))
        quantidade = int(input('Quantidade em estoque:'))
    except:
        return False    
    produto['Nome'] = nome
    produto['Preço'] = preco
    produto['Quantidade'] = quantidade    
    produtos['Produto'] = produto.copy()
    lista(produtos.copy())
    produtos.clear()
    linha()
    print('\033[32mPRODUTO ADICIONADO!\033[m'.center(50))

def ver():
    if len(prod) == 0:
        erro('Nenhum produto cadastrado ainda.')
    else:
        linha()
        print('PRODUTOS' .center(40))
        linha()
        print('PRODUTO     | PREÇO      | QUANTIDADE')
        print('_' *40)
        for c, i in enumerate(prod):
            for p in i:
                print(f'{prod[c]['Produto']['Nome'] :<11} | {dinheiro(prod[c]['Produto']['Preço']) :<10} | {prod[c]['Produto']['Quantidade'] :<4} UN')
