from utilitarios import *

#categorias
cat_receitas = cadastrar_categoria("Receita")
cat_despesa = cadastrar_categoria("Despesa")

#transacoes
cadastrar_transacao(desc="salario 8/24",valor = 706, categoria=cat_receitas)
cadastrar_transacao(desc="bavs e transporte",valor = 1006, categoria=cat_receitas)
cadastrar_transacao(desc="fatura 8/24",valor = -500, categoria=cat_despesa)
cadastrar_transacao(desc="uber 1/9/24",valor = -15, categoria=cat_despesa)

listar_transacoes()

saldo_total()


