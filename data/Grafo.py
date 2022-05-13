"""—————————————————
    Clase Grafo.
—————————————————"""
from data.Vertice import Vertice
from data.Arista import Arista


class Grafo:

    """——————————————————————00——————————————————————CONSTRUCTOR—————————————————————————————————————————————————————"""

    def __init__(self):
        self.lista_vertices = []
        self.lista_aristas = []

    def get_lista_vertices(self):
        return self.lista_vertices

    def get_lista_aristas(self):
        return self.lista_aristas
    """——————————————————————01——————————————————————VÉRTICES————————————————————————————————————————————————————————"""

    def ingresar_vertice(self, dato):
        if not self.existe_vertice(dato, self.lista_vertices):
            self.lista_vertices.append(Vertice(dato))

    def mostrar_vertices(self):
        for i in range(len(self.lista_vertices)):
            print("{0}".format(self.lista_vertices[i].get_dato()))
        return False

    def obtener_vertice(self, origen, lista):
        for i in range(len(lista)):
            if origen == lista[i].get_dato():
                return lista[i]

    def existe_vertice(self, dato, lista_vertices):
        for i in range(len(lista_vertices)):
            if dato == lista_vertices[i].get_dato():
                return True
        return False

    """——————————————————————02——————————————————————ARISTAS—————————————————————————————————————————————————————————"""

    def ingresar_arista(self, origen, destino, peso):
        """
        Entre origen y destino hay un peso de arista, se verifica que no haya un dato previo conexo entre los mismos y
        de ser posible da append con la arista y luego obtiene el vértice necesitado para darle el destino.
        :param origen: dato String.
        :param destino: dato String.
        :param peso: dato int.
        :return: no.
        """
        if not self.verificar_lista_arista(origen, destino, self.lista_aristas):
            if self.existe_vertice(origen, self.lista_vertices) and self.existe_vertice(destino, self.lista_vertices):
                self.lista_aristas.append(Arista(origen, destino, peso))
                self.obtener_vertice(origen, self.lista_vertices).get_lista_adyacentes().append(destino)
                return True
        return False

    def verificar_lista_arista(self, origen, destino, lista):
        """
        Verifica que el dato origen y destino de la lista, sea de vértice si sea correspondiente.
        :param origen: dato String.
        :param destino: dato String.
        :param lista: de vértices u aristas.
        :return: true sean correspondientes.
        """
        for i in range(len(lista)):
            if origen == lista[i].get_origen() and destino == lista[i].get_destino():
                return True
        return False

    def mostrar_aristas(self):
        for i in range(len(self.lista_aristas)):
            print("| Origen: {0}  →  Destino: {1}  |  Peso: {2} |"
                  .format(self.lista_aristas[i].get_origen(),
                          self.lista_aristas[i].get_destino(),
                          self.lista_aristas[i].get_peso()))

    def mostrar_adyacencias(self):
        for i in range(len(self.lista_vertices)):
            print("| vértice: {0} |  Adyacencias: {1} |"
                  .format(self.lista_vertices[i].get_dato(),
                          self.lista_vertices[i].getListaAdyacencias()))

    """——————————————————————03——————————————————————FUNCIONES———————————————————————————————————————————————————————"""

    def existen_pozos(self):
        for i in range(len(self.lista_vertices)):
            if not self.lista_vertices[i].get_lista_adyacentes():
                return print("Pozo --> {0}".format(self.lista_vertices[i].get_dato()))
        return print("El grafo no tiene Pozos")

    def existen_fuentes(self):
        for i in range(len(self.lista_vertices)):
            if self.lista_vertices[i].get_lista_adyacentes():
                return print("Fuente --> {0}".format(self.lista_vertices[i].get_dato()))
        return print("El grafo no tiene Fuentes")
