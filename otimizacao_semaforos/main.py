import json
from core.a_star import a_star
from core.semaforo_model import EstadoSemaforo, gerar_vizinhos, teste_objetivo
from core.visualization import plot_estado
# Função heurística simples de exemplo (substitua conforme necessário)
def heuristica(estado):
    # Exemplo: retorna a soma das filas como heurística
    return sum(estado.filas)

# Carrega configurações
with open("data/config_cruzamento.json") as f:
    config = json.load(f)

estado_inicial = EstadoSemaforo(
    semaforo="Sem1",
    tempo_restante=config["tempo_verde_padrao"],
    filas=[10, 15]
)

# Executa A*
solucao = a_star(estado_inicial, heuristica, gerar_vizinhos, teste_objetivo)

# Mostra resultado final
plot_estado(solucao[-1])