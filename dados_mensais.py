import pandas as pd

meus_dados_mensais = pd.read_csv('dados_vendas.csv')

meus_dados_mensais['Mês'] = pd.to_datetime(meus_dados_mensais['Data']).dt.month

total_vendas_por_produto_mes = meus_dados_mensais.groupby(['Produto', 'Mês'])['Quantidade'].sum().reset_index()

total_vendas_por_produto_mes.to_csv('vendas_por_produto_por_mes.csv', index= False)