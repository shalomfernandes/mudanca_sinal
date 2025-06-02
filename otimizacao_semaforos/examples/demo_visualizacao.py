import sys
from pathlib import Path

# Adiciona o diretório raiz ao PATH para resolver imports
sys.path.append(str(Path(__file__).parent.parent))

from core.a_star import a_star
from core.semaforo_model import EstadoSemaforo, gerar_vizinhos, teste_objetivo
from core.cost_heuristic import heuristica
from core.visualization import animar_solucao

# Configuração inicial
estado_inicial = EstadoSemaforo(semaforo="Sem1", tempo_restante=5, filas=[10, 15])
solucao = a_star(estado_inicial, heuristica, gerar_vizinhos, teste_objetivo)

# Animação
animar_solucao(solucao)