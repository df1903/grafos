class Arista:

    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso

    def get_origen(self):
        return self.origen

    def set_origen(self, origen):
        self.origen = origen

    def get_peso(self):
        return self.peso

    def set_peso(self, peso):
        self.peso = peso

    def get_destino(self):
        return self.destino

    def set_destino(self, destino):
        self.destino = destino
