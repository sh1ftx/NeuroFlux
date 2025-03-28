# FILE: /sistema_previsao/sistema_previsao/src/utils/funcoes_auxiliares.py

# Funções auxiliares para o sistema de previsão

# Divisor para organização
# ========================

import matplotlib.pyplot as plt
import numpy as np

# Função para visualizar os dados
def visualizar_dados(x, y, titulo='Visualização de Dados', xlabel='X', ylabel='Y'):
    """
    Plota os dados fornecidos.

    Parâmetros:
    x : array-like
        Dados do eixo X.
    y : array-like
        Dados do eixo Y.
    titulo : str
        Título do gráfico.
    xlabel : str
        Rótulo do eixo X.
    ylabel : str
        Rótulo do eixo Y.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()

# Divisor para organização
# ========================

# Função para calcular métricas de desempenho
def calcular_metricas(y_true, y_pred):
    """
    Calcula métricas de desempenho para as previsões.

    Parâmetros:
    y_true : array-like
        Valores reais.
    y_pred : array-like
        Valores previstos.

    Retorna:
    dict
        Dicionário com as métricas de desempenho.
    """
    erro_medio = np.mean(np.abs(y_true - y_pred))
    erro_quadratico_medio = np.sqrt(np.mean((y_true - y_pred) ** 2))
    
    return {
        'Erro Médio': erro_medio,
        'Erro Quadrático Médio': erro_quadratico_medio
    }