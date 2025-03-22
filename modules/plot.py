import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm

# Gráfico
def plot_results_memory(df):

    fig = px.scatter(
        df, 
        y=df['memory_result'], 
        x=df['time_result'], 
        title='Memoria', 
        trendline='ols',
        color=df['memory_result']
    )
    
    return fig

def plot_results_memory_for_time(df):
    fig = go.Figure()   

    # Memoria
    fig.add_trace(go.Scatter(
        y= df["time_result"], 
        x= df["memory_result"], 
        mode= 'lines+markers', 
        name= "Memória Usada",
        yaxis= "y1",
        line= dict(color="red")
    ))


    fig.update_layout(
        title="Comparação de Memória e Tempo de Execução",
        xaxis=dict(title="Tempo de Execução"),                  # X
        yaxis=dict(                                        # Y1
            title="Memória Usada (MiB)",
            side="left"
        )
    )

    return fig

def plot_results_values(df):
    fig = go.Figure()

    # Memoria
    fig.add_trace(go.Scatter(
        x= df.index, 
        y= df["memory_result"], 
        mode= 'lines+markers', 
        name= "Memória Usada",
        yaxis= "y1",
        line= dict(color="red")
    ))

    # Execução
    fig.add_trace(go.Scatter(
        x= df.index, 
        y= df["time_result"], 
        mode= 'lines+markers', 
        name= "Tempo de Execução",
        yaxis= "y2",
        line=dict(color="blue")
    ))

    fig.update_layout(
        title="Comparação de Memória e Tempo de Execução",
        xaxis=dict(title="Valor Somado"),                  # X
        yaxis=dict(                                        # Y1
            title="Memória Usada (MiB)",
            side="left"
        ),
        yaxis2=dict(                                       # Y2
            title="Tempo de execução (segundos)",
            overlaying="y",
            side="right"
        )
    )

    return fig