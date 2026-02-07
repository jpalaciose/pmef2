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

def GenQuadMesh_2D(Lx, Ly, ne):
    '''
    Función que crea el mallado de elementos rectangulares en una sección
    rectangular.
    Lx  : Longitud en direccion X
    Ly  : Longitud en direccion Y
    ne:     Número de elementos a crear.
    '''
    if min(Lx, Ly) == Lx:
        nx = ne
        ms_x = Lx/nx
        ny = round(Ly/ms_x)
        ms_y = Ly/ny
    else:
        ny = ne
        ms_y = Ly/ny
        nx = round(Lx/ms_y)
        ms_x = Lx/nx
    # print(ms_x,ms_y,nx,ny)
    ni		= 0
    noNodes = (nx+1)*(ny+1)
    x	= np.zeros((noNodes, 2),'float')
    for j in range(ny+1):
        for i in range(nx+1):
            x[ni]= (ms_x*i,ms_y*j)
            ni = ni + 1
    noElements = nx*ny
    connect = np.zeros((noElements, 4), 'i4')
    k = 0
    for i in range(0, ny):
        for j in range(0, nx):
            connect[k, 0] = j+((i)*(nx+1))
            connect[k, 1] = j+((i)*(nx+1))+ 1
            connect[k, 2] = j+((i+1)*(nx+1))+1
            connect[k, 3] = j+((i+1)*(nx+1))
            k = k + 1
    class Mesh:
        NN 		= noNodes
        NC 		= noElements
        Nodos 	= x
        Conex 	= connect
    return Mesh


def GenBrickMesh_3D(L, B, H, lc):
    '''Crea la malla de un elemento rectangular con códigos programados en Python.
    L  : Longitud del elemento
    B  : Ancho del elemento
    H  : Altura del elemento
    lc : Número de elementos en la dirección más corta entre L, B o H.
    '''
    # Define la cantidad de elementos y sus dimensiones en ambas direcciones.
    if min((L, B, H)) == L:
        nx = lc
        ms_x = L / nx
        ny = round(B / ms_x)
        ms_y = B / ny
        nz = round(H / ms_x)
        ms_z = H / nz
    elif min((L, B, H)) == B:
        ny = lc
        ms_y = B / ny
        nx = round(L / ms_y)
        ms_x = L / nx
        nz = round(H / ms_y)
        ms_z = H / nz
    else:
        nz = lc
        ms_z = H / nz
        ny = round(B / ms_z)
        ms_y = B / ny
        nx = round(L / ms_z)
        ms_x = L / nx

    # Imprime los resultados
    print('=' * 16 + 'Mesh' + '=' * 16)
    print("nx = {}, dx = {:.2e}, ny = {}, dy = {:.2e}, nz = {}, dz = {:.2e}".format(nx, ms_x, ny, ms_y, nz, ms_z))

    # Define los nodos de la malla
    noNodes = (nx + 1) * (ny + 1) * (nz + 1)
    Nodes = np.zeros((noNodes, 3),'float64')
    ni = 0
    for i in range(nz + 1):
        for j in range(ny + 1):
            for k in range(nx + 1):
                Nodes[ni] = (ms_x * k, ms_y * j, ms_z * i)
                ni = ni + 1

    # Se establecen las conexiones entre los nodos de la malla para definir los elementos finitos
    noElem = nx * ny * nz
    connect = np.zeros((noElem, 8), 'int')
    cont = 0
    for k in range(0, nz):
        for i in range(0, ny):
            for j in range(0, nx):
                connect[cont, 0] = j + (i * (nx + 1)) + (k * (nx + 1) * (ny + 1))
                connect[cont, 1] = j + (i * (nx + 1)) + (k * (nx + 1) * (ny + 1)) + 1
                connect[cont, 2] = j + ((i + 1) * (nx + 1)) + ((k) * (nx + 1) * (ny + 1)) + 1
                connect[cont, 3] = j + ((i + 1) * (nx + 1)) + ((k) * (nx + 1) * (ny + 1))
                connect[cont, 4] = j + (i * (nx + 1)) + ((k + 1) * (nx + 1) * (ny + 1))
                connect[cont, 5] = j + (i * (nx + 1)) + ((k + 1) * (nx + 1) * (ny + 1)) + 1
                connect[cont, 6] = j + ((i + 1) * (nx + 1)) + ((k + 1) * (nx + 1) * (ny + 1)) + 1
                connect[cont, 7] = j + ((i + 1) * (nx + 1)) + ((k + 1) * (nx + 1) * (ny + 1))
                cont += 1
    # Se agrega los parámetros calculados al diccionario Data
    class Mesh:
        NN = noNodes
        Nodos = Nodes
        NC = noElem
        Conex = connect
    return Mesh

    