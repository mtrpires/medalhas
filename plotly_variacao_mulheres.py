# -*- coding: utf-8
import pandas as pd
import numpy as np
import csv
import plotly as py
import plotly.graph_objs as go
from datetime import datetime

py.plotly.sign_in('mtrpires', 'cd7lus33e2')

df = pd.read_csv('data/mulheres_olimpiadas.csv')

trace1 = go.Scatter(
    x = df['Ano'],
    y = df['Variação (em relação ao ano anterior)'],
    mode = 'lines',
    name = 'Femininos',
    line = dict(
        color = ('rgb(170,190,146)'),
        width = 3
    )
)

layout = go.Layout(
    title='Variação do número de mulheres nas Olimpíadas',
    titlefont = dict(size = 'auto'),
    xaxis=dict(
        zeroline = False,
        showexponent='all',
        range = [1896, 2020],
        title='Ano',
        titlefont=dict(
            family='Arial',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        zeroline = False,
        showexponent = 'all',
        title='Número de mulheres<br />(em relação ao ano anterior)',
        titlefont=dict(
            family='Arial',
            size=18,
            color='#7f7f7f'
        )
    )
)

data = [trace1]
fig = go.Figure(data=data, layout=layout)
#py.offline.plot(fig, filename='variacao mulheres')
py.plotly.iplot(fig, filename='variacao mulheres')
