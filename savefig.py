import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv('dados_vendas.csv')

total_vendas_por_produtos = df.groupby('Produto')['Quantidade'].sum().reset_index()

plt.bar(total_vendas_por_produtos['Produto'], total_vendas_por_produtos['Quantidade'])
plt.xlabel('Produtos')
plt.xlabel('Total de Vendas')
plt.title('Total de Vendas por Produtos')

plt.savefig('grafico.png')
plt.show()
