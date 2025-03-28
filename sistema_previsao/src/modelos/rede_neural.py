from sklearn.neural_network import MLPRegressor
import pandas as pd

# =========================================
# Classe para o modelo de rede neural
# =========================================
class RedeNeural:
    def __init__(self, camadas_ocultas=(5,), max_iter=1000):
        """
        Inicializa o modelo de rede neural com camadas ocultas e iterações máximas.
        
        :param camadas_ocultas: Tupla com o número de neurônios em cada camada oculta.
        :param max_iter: Número máximo de iterações para o treinamento.
        """
        self.modelo = MLPRegressor(hidden_layer_sizes=camadas_ocultas, max_iter=max_iter)

    def treinar(self, dados, alvos):
        """
        Treina o modelo com os dados históricos.
        
        :param dados: Dados de entrada (features) para o treinamento.
        :param alvos: Valores alvo (target) correspondentes aos dados de entrada.
        """
        self.modelo.fit(dados, alvos)

    def prever(self, novos_dados):
        """
        Faz previsões com o modelo treinado.
        
        :param novos_dados: Dados de entrada para os quais se deseja prever os valores.
        :return: Previsões feitas pelo modelo.
        """
        return self.modelo.predict(novos_dados)

    def salvar_modelo(self, caminho):
        """
        Salva o modelo treinado em um arquivo.
        
        :param caminho: Caminho do arquivo onde o modelo será salvo.
        """
        import joblib
        joblib.dump(self.modelo, caminho)

    def carregar_modelo(self, caminho):
        """
        Carrega um modelo treinado de um arquivo.
        
        :param caminho: Caminho do arquivo de onde o modelo será carregado.
        """
        import joblib
        self.modelo = joblib.load(caminho)