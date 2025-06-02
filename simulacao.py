import pygame
from simulador.semaforo import Semaforo
from simulador.carro import Carro
from simulador.sensor import Sensor
import random

class Simulador:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Simulador de Semáforo Inteligente")
        self.clock = pygame.time.Clock()
        self.rodando = True

        self.semaforos = {v: Semaforo(v) for v in ['N', 'S', 'L', 'O']}
        self.sensores = {v: Sensor() for v in ['N', 'S', 'L', 'O']}
        self.carros = []

    def desenhar(self):
        self.tela.fill((255, 255, 255))
        for v, s in self.semaforos.items():
            pos = {'N':(275,50), 'S':(275,500), 'L':(50,275), 'O':(500,275)}[v]
            pygame.draw.rect(self.tela, s.cor(), (*pos, 50, 50))

        for c in self.carros:
            pygame.draw.rect(self.tela, (0, 0, 255), (*c.pos, 20, 20))

    def atualizar(self):
        # Geração aleatória de novos carros
        if random.random() < 0.05:
            self.carros.append(Carro(random.choice(['N', 'S', 'L', 'O'])))

        # Atualização dos sensores e semáforos
        for via, sensor in self.sensores.items():
            ativo = sensor.detectar(self.carros, via)
            self.semaforos[via].atualizar_estado(ativo)

        # Movimento dos carros
        for c in self.carros:
            c.mover(self.semaforos[c.via])

        # Remove carros que saíram da tela
        self.carros = [c for c in self.carros if 0 <= c.pos[0] <= 600 and 0 <= c.pos[1] <= 600]

    def executar(self):
        while self.rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False

            self.atualizar()
            self.desenhar()

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
