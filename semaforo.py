class Semaforo:
    def __init__(self):
        self.estado = 'VERTICAL'
        self.tempo_verde_min = 90     # 3s em frames
        self.tempo_verde_max = 300    # 10s em frames
        self.tempo_verde = self.tempo_verde_min
        self.tempo_restante = self.tempo_verde
        self.filas = {'VERTICAL': 0, 'HORIZONTAL': 0}

    def atualizar(self, fila_v, fila_h):
        self.filas['VERTICAL'] = fila_v
        self.filas['HORIZONTAL'] = fila_h

        self.tempo_restante -= 1
        if self.tempo_restante <= 0:
            self.trocar()

    def trocar(self):
        fila_v = self.filas['VERTICAL']
        fila_h = self.filas['HORIZONTAL']

        # Decide qual sentido priorizar com base na maior fila
        if fila_v == 0 and fila_h == 0:
            # Nenhuma fila, mantém o estado atual com tempo mínimo
            self.tempo_verde = self.tempo_verde_min
        elif fila_v >= fila_h:
            self.estado = 'VERTICAL'
            self.tempo_verde = self.calcular_tempo(fila_v)
        else:
            self.estado = 'HORIZONTAL'
            self.tempo_verde = self.calcular_tempo(fila_h)

        self.tempo_restante = self.tempo_verde

    def calcular_tempo(self, fila):
        """Ajusta o tempo conforme o tamanho da fila, entre tempo mínimo e máximo."""
        if fila == 0:
            return self.tempo_verde_min
        tempo = self.tempo_verde_min + fila * 15  # +0,5s por carro
        return min(tempo, self.tempo_verde_max)

    def esta_verde(self, direcao):
        return self.estado == direcao

    def cor_para(self, direcao):
        return (0, 255, 0) if self.estado == direcao else (255, 0, 0)

    def tempo_para_mostrar(self, direcao):
        if self.estado == direcao:
            return self.tempo_restante // 30
        return 0
