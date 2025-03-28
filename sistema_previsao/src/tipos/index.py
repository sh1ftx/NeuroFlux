# Conteúdo do arquivo: /sistema_previsao/sistema_previsao/src/tipos/index.py

# Este arquivo define tipos personalizados ou interfaces utilizados em todo o projeto,
# garantindo segurança de tipos e clareza no código.

from typing import List, Dict, Any

# Definição de um tipo para representar dados históricos
DadosHistoricos = List[Dict[str, Any]]

# Definição de um tipo para representar previsões
Previsao = Dict[str, float]

# Definição de um tipo para representar o modelo de previsão
ModeloPrevisao = Any  # Pode ser substituído por um tipo mais específico conforme necessário

# Fim do arquivo.