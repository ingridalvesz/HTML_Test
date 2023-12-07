import pandas as pd
# importando a biblioteca pandas e denominando-a de pd

dados_html = pd.read_html('filmes_wikipedia.html')
dados_html
# criando uma variável chamada dados_html para ler os filmes_wikipedia o qual estão em HTML

type(dados_html)
# para saber os tipos dos meus dados_html

len(dados_html)
# para saber a quantidade de dados_html

top_filmes = dados_html[1]
top_filmes
# criando uma variável chamada de top_filmes para utilizar uma tabela específica [1], que no caso é a segunda da dados_html

top_filmes.to_html('top_filmes.html')
top_filmes.to_csv('top_filmes.csv')
# somente para salvar os dados em arquivos distintos



# %%