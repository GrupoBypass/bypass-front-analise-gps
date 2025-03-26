from modules import plot as plt, save as s
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)



app.layout = html.Div(
    children=[

        html.Div(
            children=[
                html.Img(
                    src="/assets/logo.png", 
                    className="imgLogo"
                ),
                html.H1('Análise de Performance de Algoritmo', style={'textAlign': 'left'}),
            ],
            className="header"
        ),
        

        html.Div(
            children=[
                html.H3('Tempo x Memória', style={'marginTop': '10px'}),
                html.P('Análise do desempenho do algoritmo para entender sua eficiência em termos de tempo de execução e consumo de memória.'),
                html.Hr()
            ],
            className="container"
        ),
        
        
        html.Div(
            children=[
                html.H4('Relação Entre Uso de Memória e Tempo de Execução'),
                html.P('Representa a relação entre memória usada e tempo de execução.'),
                html.P('A linha de tendência mostra que o aumento da memória ao longo do tempo não é perfeitamente linear.')
            ],
            className="container"
        ),
        
        dcc.Graph(
            id='graph-1',
            figure=plt.plot_results_memory(s.get_results()),
            className="graphs"
        ),

        
        html.Div(
            children=[
                html.Hr(),
                html.H4('Relação entre Memória Usada e Tempo de Execução'),
                html.P('Representa o consumo de memória (em MiB) ao longo do tempo de execução (segundos).'),
                html.P('A curva é crescente, indicando que o consumo de memória aumenta progressivamente com o tempo.')
            ],
            className="container"
        ),
        
        dcc.Graph(
            id='graph-2',
            figure=plt.plot_results_memory_for_time(s.get_results()),
            className="graphs"
        ),
        
        
        html.Div(
            children=[
                html.H4('Comparação de Memória e Tempo de Execução por Valor Somado'),
                html.P('Compara Memória Usada (linha vermelha) e Tempo de Execução (linha azul) contra uma métrica chamada Valor Somado.'),
                html.P('As duas curvas sobem de forma similar, sugerindo que ambas crescem conforme a métrica do eixo X aumenta.')
            ],
            className="container"
        ),
        
        dcc.Graph(
            id='graph-3',
            figure=plt.plot_results_values(s.get_results()),
            className="graphs"
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
