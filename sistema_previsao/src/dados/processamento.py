from pandas import read_csv
from sklearn.preprocessing import MinMaxScaler

# -------------------------------------------
# Módulo de Processamento de Dados
# Este módulo é responsável por carregar e pré-processar os dados históricos
# a partir de arquivos CSV. Inclui funções para limpeza, normalização e
# preparação dos dados para o treinamento da rede neural.
# -------------------------------------------

def carregar_dados(caminho_arquivo):
    """
    Carrega os dados de um arquivo CSV.

    Parâmetros:
    caminho_arquivo (str): O caminho para o arquivo CSV.

    Retorna:
    DataFrame: Dados carregados em um DataFrame do pandas.
    """
    dados = read_csv(caminho_arquivo)
    return dados

def limpar_dados(dados):
    """
    Limpa os dados removendo valores nulos e duplicados.

    Parâmetros:
    dados (DataFrame): O DataFrame com os dados a serem limpos.

    Retorna:
    DataFrame: Dados limpos.
    """
    dados = dados.dropna()  # Remove valores nulos
    dados = dados.drop_duplicates()  # Remove duplicatas
    return dados

def normalizar_dados(dados):
    """
    Normaliza os dados para o intervalo [0, 1].

    Parâmetros:
    dados (DataFrame): O DataFrame com os dados a serem normalizados.

    Retorna:
    DataFrame: Dados normalizados.
    """
    scaler = MinMaxScaler()
    dados_normalizados = scaler.fit_transform(dados)
    return dados_normalizados

def preparar_dados(caminho_arquivo):
    """
    Carrega, limpa e normaliza os dados a partir de um arquivo CSV.

    Parâmetros:
    caminho_arquivo (str): O caminho para o arquivo CSV.

    Retorna:
    DataFrame: Dados preparados para o treinamento.
    """
    dados = carregar_dados(caminho_arquivo)
    dados = limpar_dados(dados)
    dados_normalizados = normalizar_dados(dados)
    return dados_normalizados