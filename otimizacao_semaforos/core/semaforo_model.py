from dataclasses import dataclass

@dataclass
class EstadoSemaforo:
    semaforo: str       # "Sem1" ou "Sem2"
    tempo_restante: int  # Tempo restante no verde
    filas: tuple         # (fila_sem1, fila_sem2)

    def __init__(self, semaforo, tempo_restante, filas):
        self.semaforo = semaforo
        self.tempo_restante = tempo_restante
        self.filas = tuple(filas)  # Use tuple para ser hashable

    def __eq__(self, other):
        return (
            isinstance(other, EstadoSemaforo) and
            self.semaforo == other.semaforo and
            self.tempo_restante == other.tempo_restante and
            self.filas == other.filas
        )

    def __hash__(self):
        return hash((self.semaforo, self.tempo_restante, self.filas))

def gerar_vizinhos(estado):
    vizinhos = []
    semaforo, tempo, filas = estado.semaforo, estado.tempo_restante, estado.filas
    
    # Ação 1: Continuar com o mesmo semáforo
    if tempo > 0:
        novas_filas = [
            max(filas[0] - 3, 0) if semaforo == "Sem1" else filas[0] + 2,
            max(filas[1] - 3, 0) if semaforo == "Sem2" else filas[1] + 2
        ]
        vizinhos.append((EstadoSemaforo(semaforo, tempo - 1, novas_filas), sum(filas)))
    
    # Ação 2: Trocar semáforo
    novoSemaforo = "Sem2" if semaforo == "Sem1" else "Sem1"
    vizinhos.append((EstadoSemaforo(novoSemaforo, 5, [filas[0] + 2, filas[1] + 2]), sum(filas) + 10))
    
    return vizinhos

def teste_objetivo(estado):
    return all(fila <= 0 for fila in estado.filas) or estado.tempo_restante <= 0