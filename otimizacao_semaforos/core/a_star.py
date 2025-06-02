import heapq
import itertools

def a_star(estado_inicial, heuristica, gerar_vizinhos, teste_objetivo):
    contador = itertools.count()  # contador único para desempate
    fila = [(0 + heuristica(estado_inicial), next(contador), 0, estado_inicial, [])]  # (f, count, g, estado, caminho)
    visitados = set()

    while fila:
        f_custo, _, g_custo, estado, caminho = heapq.heappop(fila)
        
        if teste_objetivo(estado):
            return caminho + [estado]
        
        if estado not in visitados:
            visitados.add(estado)
            for vizinho, custo in gerar_vizinhos(estado):
                novo_g_custo = g_custo + custo
                heapq.heappush(
                    fila,
                    (novo_g_custo + heuristica(vizinho), next(contador), novo_g_custo, vizinho, caminho + [estado])
                )
    return None