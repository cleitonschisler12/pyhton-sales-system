from estoque import *

def linha():
    print('-' *40)

def cor(número, palavra):
    print(f'\033[33m{número} \033[34m{palavra}\033[m')

def erro(msg):
    print(f'\033[31m{msg}\033[m')

def dinheiro(preço):
    if preço:
        a = f'{preço:.2f}'.replace('.', ',')
        b = 'R$' + a
        return b 
    
        

