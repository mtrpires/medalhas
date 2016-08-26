# -*- coding: utf-8
import pandas as pd
import numpy as np
import csv
import plotly as py
import plotly.graph_objs as go
from datetime import datetime

py.plotly.sign_in('mtrpires', 'cd7lus33e2')

df = pd.read_csv('data/eventos_femininos.csv')

trace1 = go.Scatter(
    x = df['Ano'],
    y = df['Femininos'],
    mode = 'lines',
    name = 'Femininos',
    line = dict(
        color = ('rgb(170,190,146)'),
        width = 3
    )
)

trace2 = go.Scatter(
    x = df['Ano'],
    y = df['Masculinos'],
    mode = 'lines',
    name = 'Masculinos',
    line = dict(
        color = ('rgb(123,108,135)'),
        width = 3
    )
)

layout = go.Layout(
    title='Eventos esportivos nos Jogos Olímpicos',
    titlefont = dict(size = 'auto'),
    xaxis=dict(
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
        showexponent = 'all',
        title='Eventos',
        titlefont=dict(
            family='Arial',
            size=18,
            color='#7f7f7f'
        )
    )
)

data = [trace1, trace2]
fig = go.Figure(data=data, layout=layout)
py.plotly.iplot(fig, filename='eventos_femininos')
