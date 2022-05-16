from clases.Grafo import *

# graph creation
grafo = Grafo()

# creation of vertices
grafo.ingresarVertice('Manizales')
grafo.ingresarVertice('Pereira')
grafo.ingresarVertice('Armenia')
grafo.ingresarVertice('Cali')
grafo.ingresarVertice('Bogota')
grafo.ingresarVertice('Cututa')
grafo.ingresarVertice('Barranquilla')
grafo.ingresarVertice('Cartagena')
grafo.ingresarVertice('Medellin')
"""_____________________________________________"""
# graph_no cycles_connected_directed
# grafo.ingresarArista('Manizales','Pereira',1)
# grafo.ingresarArista('Manizales','Bogota',8)
# grafo.ingresarArista('Manizales','Medellin',4)
# grafo.ingresarArista('Pereira','Armenia',3)
# grafo.ingresarArista('Armenia','Cali',4)
# grafo.ingresarArista('Armenia','Bogota',3)
# grafo.ingresarArista('Medellin','Bogota',4)
# grafo.ingresarArista('Bogota','Cututa',7)
# grafo.ingresarArista('Bogota','Cartagena',6)
# grafo.ingresarArista('Cartagena','Barranquilla',1)
# grafo.ingresarArista('Barranquilla','Cututa',12)

"""_____________________________________________"""
# graph_no cycles_no connected_directed
# grafo.ingresarArista('Manizales','Pereira',1)
# grafo.ingresarArista('Manizales','Bogota',8)
# grafo.ingresarArista('Manizales','Medellin',4)
# grafo.ingresarArista('Pereira','Armenia',3)
# grafo.ingresarArista('Armenia','Cali',4)
# grafo.ingresarArista('Armenia','Bogota',3)
# grafo.ingresarArista('Medellin','Bogota',4)
# grafo.ingresarArista('Cartagena','Barranquilla',1)
# grafo.ingresarArista('Barranquilla','Cututa',12)

"""_____________________________________________"""
# graph_cycles_connected_no directed
grafo.ingresarArista('Manizales','Pereira',1)
grafo.ingresarArista('Pereira','Manizales',1)
grafo.ingresarArista('Manizales','Bogota',8)
grafo.ingresarArista('Bogota','Manizales',8)
grafo.ingresarArista('Manizales','Medellin',4)
grafo.ingresarArista('Medellin','Manizales',4)
grafo.ingresarArista('Pereira','Armenia',3)
grafo.ingresarArista('Armenia', 'Pereira',3)
grafo.ingresarArista('Armenia','Cali',4)
grafo.ingresarArista('Cali','Armenia',4)
grafo.ingresarArista('Armenia','Bogota',3)
grafo.ingresarArista('Bogota','Armenia',3)
grafo.ingresarArista('Medellin','Bogota',4)
grafo.ingresarArista('Bogota','Medellin',4)
grafo.ingresarArista('Bogota','Cututa',7)
grafo.ingresarArista('Cututa','Bogota',7)
grafo.ingresarArista('Bogota','Cartagena',6)
grafo.ingresarArista('Cartagena','Bogota',6)
grafo.ingresarArista('Cartagena','Barranquilla',1)
grafo.ingresarArista('Barranquilla','Cartagena',1)
grafo.ingresarArista('Barranquilla','Cututa',12)
grafo.ingresarArista('Cututa','Barranquilla',12)

"""_____________________________________________"""
# graph_cycles_no connected_no directed
# grafo.ingresarArista('Manizales','Pereira',1)
# grafo.ingresarArista('Pereira','Manizales',1)
# grafo.ingresarArista('Manizales','Bogota',8)
# grafo.ingresarArista('Bogota','Manizales',8)
# grafo.ingresarArista('Manizales','Medellin',4)
# grafo.ingresarArista('Medellin','Manizales',4)
# grafo.ingresarArista('Pereira','Armenia',3)
# grafo.ingresarArista('Armenia', 'Pereira',3)
# grafo.ingresarArista('Armenia','Cali',4)
# grafo.ingresarArista('Cali','Armenia',4)
# grafo.ingresarArista('Armenia','Bogota',3)
# grafo.ingresarArista('Bogota','Armenia',3)
# grafo.ingresarArista('Medellin','Bogota',4)
# grafo.ingresarArista('Bogota','Medellin',4)
# grafo.ingresarArista('Cartagena','Barranquilla',1)
# grafo.ingresarArista('Barranquilla','Cartagena',1)
# grafo.ingresarArista('Barranquilla','Cututa',12)
# grafo.ingresarArista('Cututa','Barranquilla',12)

"""_____________________________________________"""
# graph_cycles_connected_directed
# grafo.ingresarArista('Manizales','Pereira',1)
# grafo.ingresarArista('Bogota','Manizales', 8)
# grafo.ingresarArista('Manizales','Medellin',4)
# grafo.ingresarArista('Pereira','Armenia',3)
# grafo.ingresarArista('Armenia','Cali',4)
# grafo.ingresarArista('Armenia','Bogota',3)
# grafo.ingresarArista('Medellin','Bogota',4)
# grafo.ingresarArista('Bogota','Cututa',7)
# grafo.ingresarArista('Bogota','Cartagena',6)
# grafo.ingresarArista('Cartagena','Barranquilla',1)
# grafo.ingresarArista('Barranquilla','Cututa',12)


"""_____________________________________________"""
# graph_cycles_no connected_directed
# grafo.ingresarArista('Manizales','Pereira',1)
# grafo.ingresarArista('Bogota','Manizales',8)
# grafo.ingresarArista('Manizales','Medellin',4)
# grafo.ingresarArista('Pereira','Armenia',3)
# grafo.ingresarArista('Armenia','Cali',4)
# grafo.ingresarArista('Armenia','Bogota',3)
# grafo.ingresarArista('Medellin','Bogota',4)
# grafo.ingresarArista('Cututa','Cartagena',13)
# grafo.ingresarArista('Cartagena','Barranquilla',1)
# grafo.ingresarArista('Barranquilla','Cututa',12)

"""_____________________________________________"""
# graph_no cycles_connected_no directed
# grafo.ingresarArista('Manizales','Pereira',1)
# grafo.ingresarArista('Pereira','Manizales',1)
# grafo.ingresarArista('Manizales','Bogota',8)
# grafo.ingresarArista('Bogota','Manizales',8)
# grafo.ingresarArista('Manizales','Medellin',4)
# grafo.ingresarArista('Medellin','Manizales',4)
# grafo.ingresarArista('Pereira','Armenia',3)
# grafo.ingresarArista('Armenia', 'Pereira',3)
# grafo.ingresarArista('Armenia','Cali',4)
# grafo.ingresarArista('Cali','Armenia',4)
# grafo.ingresarArista('Bogota','Cartagena',4)
# grafo.ingresarArista('Cartagena','Bogota',6)
# grafo.ingresarArista('Cartagena','Barranquilla',1)
# grafo.ingresarArista('Barranquilla','Cartagena',1)
# grafo.ingresarArista('Barranquilla','Cututa',12)
# grafo.ingresarArista('Cututa','Barranquilla',12)

"""_____________________________________________"""
# graph_no cycles_no connected_no directed
# grafo.ingresarArista('Manizales','Pereira',1)
# grafo.ingresarArista('Pereira','Manizales',1)
# grafo.ingresarArista('Manizales','Bogota',8)
# grafo.ingresarArista('Bogota','Manizales',8)
# grafo.ingresarArista('Manizales','Medellin',4)
# grafo.ingresarArista('Medellin','Manizales',4)
# grafo.ingresarArista('Pereira','Armenia',3)
# grafo.ingresarArista('Armenia', 'Pereira',3)
# grafo.ingresarArista('Armenia','Cali',4)
# grafo.ingresarArista('Cali','Armenia',4)
# grafo.ingresarArista('Cartagena','Barranquilla',1)
# grafo.ingresarArista('Barranquilla','Cartagena',1)
# grafo.ingresarArista('Barranquilla','Cututa',12)
# grafo.ingresarArista('Cututa','Barranquilla',12)

grafo.existenPozos()