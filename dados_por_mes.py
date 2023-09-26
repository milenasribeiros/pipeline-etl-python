import pandas as pd
import matplotlib.pyplot as plt

dados_vendas_por_produto_mes = pd.read_csv('vendas_por_produto_por_mes.csv')

fig, ax = plt.subplots(figsize=(10, 6))

produtos = dados_vendas_por_produto_mes['Produto'].unique()
for produto in produtos:
    dados_produto = dados_vendas_por_produto_mes[dados_vendas_por_produto_mes['Produto'] == produto]
    plt.bar(dados_produto['Mês'], dados_produto['Quantidade'], label=produto)

plt.xlabel('Mês')
plt.ylabel('Quantidade de Vendas')
plt.title('Vendas por Mês de Cada Produto')
plt.legend()

plt.savefig('grafico_por_mes.png')
plt.show()