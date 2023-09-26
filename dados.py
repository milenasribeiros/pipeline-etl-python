import pandas as pd
import random

produtos = ['Batom', 'Sombra de Olhos', 'Base', 'Rimel', 'Blush']

dados_vendas = []
for cliente in range(500):
    produto = random.choice(produtos)
    data = f"2023-{random.randint(1, 12):02d}-{random.randint(1,28):02d}"
    quantidade = random.randint(1, 10)
    preco = round(random.randint(5, 50), 2)
    dados_vendas.append([produto, data, quantidade, preco])

df = pd.DataFrame(dados_vendas, columns=['Produto', 'Data', 'Quantidade', 'Preco'])

df.to_csv('dados_vendas.csv', index=False)