import numpy as np
from scipy.sparse import lil_matrix, csr_matrix
from time import time


# Empezar con la función ShapeFunction
# Definir para elementos Barra: Bar1 y BarB (line en meshio)
# Definir para elementos 2D: Tri3, Quad4, Quad9 (triangle, quad4, quad9 en meshio)
# Definir para elementos Shell: ...
# Definir para elementos 3D: Brick, Tet4, Tet10 (hexahedro, tetra, tetra10 en meshio)

# EMPEZAR CON EL ELEMNTO TETRA10 Y ANALISIS NO LINEAL CON RAMBERG OSGOOD
# luego tratar de entender el caso de albanileria

# verificar elemento por elemento