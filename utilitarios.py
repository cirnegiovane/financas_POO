from categorias import Categoria
from transacoes import Transacao

lista_cat = []
lista_transacoes = []

def cadastrar_categoria(nome):
    nova_cat = Categoria(nome = nome)
    lista_cat.append(nova_cat)
    pass

def cadastrar_transacao(desc,valor,categoria):
    nova_transacao = Transacao(desc = desc, valor = valor, categoria = categoria)
    lista_transacoes.append(nova_transacao)
    pass

def saldo_total():
    total = 0
    for t in lista_transacoes:
        total += t.valor
    print(f"Total: R$: {total}")
    pass

def listar_transacoes():
    for t in lista_transacoes:
        print("-"*30)
        if(t.valor>0):
            print(f"Entrou R${t.valor}, descrição: {t.desc}.")
        else:
            print(f"Saiu R${t.valor}, descrição: {t.desc}.")
        print("-"*30)


