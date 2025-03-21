import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from scipy import stats

def plot_results(df):
    # df['values'] = np.log(df['memory_result'])
    # fig = px.line(df, y= df['memory_result'], x=df.index, title='Life expectancy in Canada')

    Q1 = df['memory_result'].quantile(0.25)
    Q3 = df['memory_result'].quantile(0.75)
    IQR = Q3 - Q1

    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    df_sem_outliers = df[(df['memory_result'] >= limite_inferior) & (df['memory_result'] <= limite_superior)]

    fig = px.line(df_sem_outliers, y='memory_result', x=df_sem_outliers.index, title='Memoria')
    print(df_sem_outliers)
    fig.show()

def plot_resultsa(df):
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

    fig.show()