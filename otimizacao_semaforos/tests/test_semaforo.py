import unittest
from core.semaforo_model import EstadoSemaforo, gerar_vizinhos

class TestSemaforo(unittest.TestCase):
    def test_troca_semaforo(self):
        estado = EstadoSemaforo("Sem1", 5, [10, 15])
        vizinhos = gerar_vizinhos(estado)
        self.assertEqual(len(vizinhos), 2)  # Deve gerar 2 ações possíveis