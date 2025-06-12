class Semaforo:
    def __init__(self):
        self.estado = 'VERTICAL'
        self.tempo_verde_min = 90     # 3s em frames
        self.tempo_verde_max = 300    # 10s em frames
        self.tempo_verde = self.tempo_verde_min
        self.tempo_restante = self.tempo_verde
        self.filas = {'VERTICAL': 0, 'HORIZONTAL': 0}
        self.rodadas = {'VERTICAL': 0, 'HORIZONTAL': 0}  # Contador de rodadas para cada direção

    def atualizar(self, fila_v, fila_h):
        self.filas['VERTICAL'] = fila_v
        self.filas['HORIZONTAL'] = fila_h

        self.tempo_restante -= 1
        if self.tempo_restante <= 0:
            self.trocar()

    def trocar(self):
        fila_v = self.filas['VERTICAL']
        fila_h = self.filas['HORIZONTAL']

        # Incrementa o contador da direção atual
        self.rodadas[self.estado] += 1

        # Verifica a direção oposta
        outra_direcao = 'HORIZONTAL' if self.estado == 'VERTICAL' else 'VERTICAL'
        fila_atual = self.filas[self.estado]
        fila_oposta = self.filas[outra_direcao]

        # Se não houver carros na direção oposta, mantém o sinal atual
        if fila_oposta == 0:
            self.tempo_verde = self.calcular_tempo(fila_atual)
        else:
            # Se houver carros na direção oposta, verifica as condições de troca
            if self.rodadas[self.estado] >= 2:
                # Força a troca após 2 rodadas
                self.estado = outra_direcao
                self.rodadas[self.estado] = 0
                self.tempo_verde = self.calcular_tempo(fila_oposta)
            elif fila_oposta > fila_atual * 1.5:  # 50% mais carros na direção oposta
                # Troca se a direção oposta tiver significativamente mais carros
                self.estado = outra_direcao
                self.rodadas[self.estado] = 0
                self.tempo_verde = self.calcular_tempo(fila_oposta)
            else:
                # Mantém o sinal atual
                self.tempo_verde = self.calcular_tempo(fila_atual)

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
