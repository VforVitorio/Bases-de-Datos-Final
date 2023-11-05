# Librerías para la creación del gráfico


import networkx as nx
import networkx as nx
import matplotlib.pyplot as plt
# Para estas dos hay que ir a la terminal y hacer pip install pydot
# Además graphviz tiene que estar instalado en el ordenador
# Enlace: https://graphviz.org/download/ (descargué la primera opción de 32 bits que dice que viene con todo)
# Luego hay que añadir la ruta de graphviz a las variables de entorno
# panel de control -> sistema y seguridad -> sistema -> configuración avanzada del sistema
# -> variables de entorno -> variables del sistema
# -> path -> editar -> nuevo -> pegar la ruta de graphviz con la carpeta bin
# Ejemplo de ruta: C:\Program Files (x86)\Graphviz2.38\bin

import pydot

from networkx.drawing.nx_pydot import graphviz_layout

# Creación de un grafo dirigido
T = nx.balanced_tree(2, 5)
# Dependiendo de lo que se ponga en prog se verá de una forma u otra
pos = graphviz_layout(T, prog="dot")

nx.draw(T, pos, with_labels=True, arrows=True)
plt.show()
