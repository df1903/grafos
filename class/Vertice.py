"""————————————————
   Vertice class
———————————————————"""
class Vertice:

    # builder
    def __init__(self, dato):
        self.dato = dato
        self.listaAdyacentes = []

    """————————————————————————————————————————————GETS | SETS————————————————————————————————————————————————————"""

    # Set - Get | dato
    def getDato(self):
        return self.dato

    def setDato(self,dato):
        self.dato = dato

    # Set - Get | lista adyacentes
    def getListaAdyacentes(self):
        return self.listaAdyacentes

    def setListaAdyacentes(self,listaAdyacentes):
        self.listaAdyacentes = listaAdyacentes


    """————————————————————————————————————————————METHODS———————————————————————————————————————————————————————"""

    # to string
    # def toString(self):
    #     s = '▌▓▒░    | dato ' + str(self.dato()) + \
    #         ' | var2: ' + str(self.var2) + \
    #         ' | var3: ' + str(self.var3) + \
    #         ' | var4: ' + str(self.var4) + \
    #         ' | var5: ' + str(self.var5)
    #     return s
