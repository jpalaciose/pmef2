import numpy as np


def LinearMesh(L,Ne,x0=0.0):
    '''
    Función que retorna nodos y conexiones para elementos finitos en 1D.

    Donde:
            L:      Longitud total de la barra.
            Ne:     Número de elementos a crear.
            x0:     Posición del primer nodo.
    '''
    # Crea arreglo de nodos
    x = np.linspace(x0,x0+L,Ne+1)
    # Crea arreglo de conexiones
    cnx = np.zeros((Ne,2),'i4')
    cnx[:,0],cnx[:,1] = range(Ne), range(1,Ne+1)
    class Mesh:
        NN = len(x)
        Nodos = x
        NC = len(cnx)
        Conex = cnx
    return Mesh

