"""————————————————
   vertice class
———————————————————"""

class Vertice:

    # builder
    def __init__(self, dato):
        self.dato = dato
        self.lista_adyacentes = []

    def get_dato(self):
        return self.dato

    def set_dato(self, dato):
        self.dato = dato

    def get_lista_adyacentes(self):
        return self.lista_adyacentes

    def set_lista_adyacentes(self, lista_adyacentes):
        self.lista_adyacentes = lista_adyacentes
