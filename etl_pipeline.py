import pandas as pd

meus_dados = pd.read_csv('dados_vendas.csv')

meus_dados['Total'] = meus_dados['Quantidade'] * meus_dados['Preco']

meus_dados.to_csv('dados_vendas_transformados.csv', index=False)
