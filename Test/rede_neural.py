from sklearn.neural_network import MLPClassifier

# Define o modelo com uma camada oculta de 4 neurônios e 1000 iterações máximas
modelo = MLPClassifier(hidden_layer_sizes=(4,), max_iter=1000)

# Treina o modelo com os dados da porta XOR
modelo.fit([[0, 0], [0, 1], [1, 0], [1, 1]], [0, 1, 1, 0])

# Faz previsões com os mesmos dados
print(modelo.predict([[0, 0], [0, 1], [1, 0], [1, 1]]))