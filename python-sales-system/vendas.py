from estoque import *

total_vendido = 0
total = 0
def venda(produto, quantidade=0):
    global total_vendido
    global total
    
    for item in prod:
        if item['Produto']['Nome'] == produto:
            valor = item['Produto']['Preço']
            estoque_atual = item['Produto']['Quantidade']
            
            if quantidade > estoque_atual:
                erro('Quantidade excedeu o estoque.')
                return False
            
            novo_estoque = estoque_atual - quantidade
            item['Produto']['Quantidade'] = novo_estoque
            total_vendido = quantidade * valor
            total += total_vendido

            linha()
            print(f'{produto}: {estoque_atual} unidades')
            print('')
            print(f'Venda: {quantidade}')
            print('')
            print(f'Estoque: {novo_estoque}')
            print(f'Total vendido: {dinheiro(total_vendido)}')
            
            return True
            
    erro('Produto não encontrado.')
    return False

def total_venda():
    try:
        if total > 0:
            print(f'As vendas totais são de {dinheiro(total)}')
            return True
    except:
         return False