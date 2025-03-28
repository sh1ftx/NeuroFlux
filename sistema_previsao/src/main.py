from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
from modelos.rede_neural import ModeloRedeNeural

# Divisor para organização
# =========================

# Função principal do sistema de previsão
def main():
    # Carrega os dados históricos
    dados_historicos = carregar_dados('data/historico.csv')
    
    # Divide os dados em características (X) e alvo (y)
    X = dados_historicos.drop('valor', axis=1)  # Supondo que a coluna 'valor' é o que queremos prever
    y = dados_historicos['valor']
    
    # Divide os dados em conjuntos de treino e teste
    X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Inicializa o modelo de rede neural
    modelo = ModeloRedeNeural()
    
    # Treina o modelo
    modelo.treinar(X_treino, y_treino)
    
    # Faz previsões
    previsoes = modelo.prever(X_teste)
    
    # Avalia o modelo
    erro = mean_squared_error(y_teste, previsoes)
    print(f'Erro quadrático médio: {erro}')
    
    # Salva as previsões em um arquivo CSV
    salvar_previsoes(previsoes, 'data/previsoes.csv')

# Função para carregar dados de um arquivo CSV
def carregar_dados(caminho):
    return pd.read_csv(caminho)

# Função para salvar previsões em um arquivo CSV
def salvar_previsoes(previsoes, caminho):
    df_previsoes = pd.DataFrame(previsoes, columns=['previsao'])
    df_previsoes.to_csv(caminho, index=False)

# Chama a função principal
if __name__ == "__main__":
    main()