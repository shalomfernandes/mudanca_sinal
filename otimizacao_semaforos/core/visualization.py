import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

def animar_solucao(solucao):
    cruzamento_size = 6
    rua_largura = 2
    carro_tam = 0.5

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-cruzamento_size, cruzamento_size)
    ax.set_ylim(-cruzamento_size, cruzamento_size)
    ax.set_aspect('equal')
    ax.axis('off')

    # Desenha as ruas
    ax.add_patch(patches.Rectangle((-cruzamento_size, -rua_largura/2), 2*cruzamento_size, rua_largura, color='gray', zorder=0))
    ax.add_patch(patches.Rectangle((-rua_largura/2, -cruzamento_size), rua_largura, 2*cruzamento_size, color='gray', zorder=0))

    # Semáforos (um para cada direção)
    semaforo1 = patches.Circle((-1.5, 1.5), 0.3, color='green')
    semaforo2 = patches.Circle((1.5, -1.5), 0.3, color='red')
    ax.add_patch(semaforo1)
    ax.add_patch(semaforo2)

    # Carros (listas de patches)
    max_carros = 10
    carros_sem1 = [patches.Rectangle((-6 + i*carro_tam*1.5, -0.8), carro_tam, carro_tam, color='blue') for i in range(max_carros)]
    carros_sem2 = [patches.Rectangle((-0.8, 6 - i*carro_tam*1.5), carro_tam, carro_tam, color='orange') for i in range(max_carros)]
    for carro in carros_sem1 + carros_sem2:
        ax.add_patch(carro)

    # Estado para fluxo extra
    fluxo_h = 0
    fluxo_v = 0

    def on_key(event):
        nonlocal fluxo_h, fluxo_v
        if event.key == 'h':
            fluxo_h += 1
        elif event.key == 'v':
            fluxo_v += 1

    fig.canvas.mpl_connect('key_press_event', on_key)

    frame_idx = [0]  # Usar lista para mutabilidade no escopo

    def update(_):
        # Mantém o frame rodando em loop
        frame_idx[0] = (frame_idx[0] + 1) % len(solucao)
        estado = solucao[frame_idx[0]]

        # Atualiza semáforos
        if estado.semaforo == "Sem1":
            semaforo1.set_color('green')
            semaforo2.set_color('red')
        else:
            semaforo1.set_color('red')
            semaforo2.set_color('green')

        # Atualiza carros da rua Sem1 (horizontal)
        fila1 = estado.filas[0] + fluxo_h
        for i, carro in enumerate(carros_sem1):
            if i < fila1:
                # Carros na fila, param antes do semáforo se vermelho
                if estado.semaforo == "Sem1" or (estado.semaforo == "Sem2" and i > 0):
                    carro.set_xy((-6 + i*carro_tam*1.5, -0.8))
                else:
                    carro.set_xy((-1.5 - carro_tam, -0.8))
            else:
                carro.set_xy((100, 100))  # Fora da tela

        # Atualiza carros da rua Sem2 (vertical)
        fila2 = estado.filas[1] + fluxo_v
        for i, carro in enumerate(carros_sem2):
            if i < fila2:
                if estado.semaforo == "Sem2" or (estado.semaforo == "Sem1" and i > 0):
                    carro.set_xy((-0.8, 6 - i*carro_tam*1.5))
                else:
                    carro.set_xy((-0.8, 1.5 + carro_tam))
            else:
                carro.set_xy((100, 100))

        return carros_sem1 + carros_sem2 + [semaforo1, semaforo2]

    ani = FuncAnimation(fig, update, frames=None, interval=400, blit=True)
    plt.show()