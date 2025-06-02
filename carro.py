import time

class Carro:
    def __init__(self, direcao):
        self.direcao = direcao
        if direcao == 'HORIZONTAL':
            self.x, self.y = 0, 290
        else:
            self.x, self.y = 290, 0
        self.passou_semaforo = False
        self.tempo_chegada = time.time()
        self.tempo_espera = 0

    def mover(self, semaforo, fila, indice):
        distancia = 25
        if self.direcao == 'HORIZONTAL':
            limite_parada = 275
            if not self.passou_semaforo and self.x + distancia >= limite_parada and not semaforo.esta_verde('HORIZONTAL'):
                self.tempo_espera = time.time() - self.tempo_chegada
                return
            if indice > 0 and fila[indice - 1].x < self.x + distancia and not fila[indice - 1].passou_semaforo:
                return
            self.x += 2
            if self.x > limite_parada:
                self.passou_semaforo = True
        else:
            limite_parada = 275
            if not self.passou_semaforo and self.y + distancia >= limite_parada and not semaforo.esta_verde('VERTICAL'):
                self.tempo_espera = time.time() - self.tempo_chegada
                return
            if indice > 0 and fila[indice - 1].y < self.y + distancia and not fila[indice - 1].passou_semaforo:
                return
            self.y += 2
            if self.y > limite_parada:
                self.passou_semaforo = True
