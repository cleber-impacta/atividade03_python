import pandas as pd

massa_dados = 'https://github.com/cleber-impacta/atividade03_python/blob/main/massa%20de%20dados/04-2020.txt?raw=true'

lista=pd.read_table(massa_dados, sep=';')
lista

"""

Mostra as 5 primeiras linhas
"""

lista.head()

"""Número de linhas e coluna"""

lista.shape

lista['despacho'].value_counts()

lista['despacho'].value_counts().plot.barh()

lista['despacho'].unique()

lista['despacho'].value_counts()

lista['despacho'].value_counts(normalize = True)

lista.describe()

pd.crosstab(lista['especie'], lista['sexo'])