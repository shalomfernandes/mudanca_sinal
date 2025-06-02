import pygame
from simulador.semaforo import Semaforo
from simulador.carro import Carro
from simulador.sensor import Sensor

def executar_simulacao():
    pygame.init()
    tela = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, 24)

    semaforo = Semaforo()
    sensor_vertical = Sensor()
    sensor_horizontal = Sensor()
    carros_vertical = []
    carros_horizontal = []

    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_h:
                    carros_horizontal.append(Carro('HORIZONTAL'))
                elif evento.key == pygame.K_v:
                    carros_vertical.append(Carro('VERTICAL'))

        sensor_vertical.fila = carros_vertical
        sensor_horizontal.fila = carros_horizontal

        fila_v = sensor_vertical.detectar()
        fila_h = sensor_horizontal.detectar()

        semaforo.atualizar(fila_v, fila_h)

        for i, carro in enumerate(carros_vertical):
            carro.mover(semaforo, carros_vertical, i)
        for i, carro in enumerate(carros_horizontal):
            carro.mover(semaforo, carros_horizontal, i)

        for lista in [carros_vertical, carros_horizontal]:
            for carro in lista[:]:
                if carro.passou_semaforo and (carro.x > 600 or carro.y > 600):
                    lista.remove(carro)

        tela.fill((255, 255, 255))

        pygame.draw.rect(tela, semaforo.cor_para('VERTICAL'), (275, 250, 20, 50))
        pygame.draw.rect(tela, semaforo.cor_para('HORIZONTAL'), (250, 275, 50, 20))

        for carro in carros_vertical:
            pygame.draw.rect(tela, (0, 0, 255), (carro.x, carro.y, 20, 20))
        for carro in carros_horizontal:
            pygame.draw.rect(tela, (255, 165, 0), (carro.x, carro.y, 20, 20))

        # Mostrar informações
        tempo_v = semaforo.tempo_para_mostrar('VERTICAL')
        tempo_h = semaforo.tempo_para_mostrar('HORIZONTAL')

        texto_v = fonte.render(f"V: {tempo_v}s | Fila: {fila_v}", True, (0, 0, 0))
        texto_h = fonte.render(f"H: {tempo_h}s | Fila: {fila_h}", True, (0, 0, 0))

        tela.blit(texto_v, (10, 10))
        tela.blit(texto_h, (10, 40))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    executar_simulacao()
