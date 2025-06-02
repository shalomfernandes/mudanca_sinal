class Sensor:
    def __init__(self):
        self.fila = []

    def detectar(self):
        return sum(1 for carro in self.fila if not carro.passou_semaforo)
