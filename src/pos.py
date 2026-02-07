import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image


# Funciones para graficar utilizando matplotlib
def graph(x,cnx,ax,color='k',d=0.01,logo=True,labels=False):
    '''
    Función que grafica los nodos y elementos del modelo.
    '''
    if logo == True:
        xrng, yrng = plt.xlim(),plt.ylim()
        L = min(xrng[1]-xrng[0],yrng[1]-yrng[0])
        im = image.imread('https://jpi-ingenieria.com/images/logoJPI.png')
        ax.imshow(im,aspect='auto',extent=(xrng[0], xrng[0]+0.2*L, yrng[0], yrng[0]+0.2*L), zorder=10,alpha=0.7)
        logo = False

    if len(x.shape)==1:
        dim = 1
        NN = len(x)
    else:
        (NN,dim) = x.shape

    if dim == 1:
        for ii in range(len(x)):
            if labels == True:
                ax.plot(x[ii],0.0,color+'o',markersize=1.5)
                ax.annotate('%i'%(ii),(x[ii],0.0),
                                xytext=(x[ii]+d,0.0+d),color='black')
        ie=0
        for e in cnx:
            xx = x[e]
            ax.plot(xx,[0.0,0.0],color,lw = 1.0,alpha=1.0)
            if labels == True:
                xa,ya = np.average(xx),0.0
                ax.annotate('%i'%(ie),(xa,ya+d),color='blue',fontsize=8.)
            ie += 1
        Lx = max(x) - min(x)
        plt.axis([np.average(x)-1.02*Lx/2,np.average(x)+1.02*Lx/2,-Lx/4,Lx/4])

    elif dim == 2:
        for ii in range(len(x)):
            if labels == True:
                ax.plot(x[ii,0],x[ii,1],'ko',markersize=1.5)
                ax.annotate('%i'%(ii),(x[ii,0],x[ii,1]),
                                xytext=(x[ii,0]+d,x[ii,1]+d),color='black')
        ie=0
        for e in cnx:
            xx = x[np.append(e,e[0])]
            ax.plot(xx[:,0],xx[:,1],'k',lw = 0.3,alpha=0.5)
            if labels == True:
                xa,ya=np.average(x[e,0]),np.average(x[e,1])
                ax.annotate('%i'%(ie),(xa,ya),color='blue',fontsize=8.)
            ie += 1

    elif dim == 3:
        for ii in range(len(x)):
            if labels == True:
                ax.plot(x[ii,0],x[ii,1],x[ii,2],color+'o',markersize=1.5)
                ax.text(x[ii,0],x[ii,1],x[ii,2],'%i'%(ii),color='black')
        ie=0
        for e in cnx:
            xx = x[[e[0],e[1],e[2],e[3],e[0],e[4],e[5],e[6],e[7],e[4]]]
            ax.plot(xx[:,0],xx[:,1],xx[:,2],color,lw = 0.3,alpha=0.5)
            ax.plot(x[[e[1],e[5]],0],x[[e[1],e[5]],1],x[[e[1],e[5]],2],'k',lw = 0.3,alpha=0.5)
            ax.plot(x[[e[2],e[6]],0],x[[e[2],e[6]],1],x[[e[2],e[6]],2],'k',lw = 0.3,alpha=0.5)
            ax.plot(x[[e[3],e[7]],0],x[[e[3],e[7]],1],x[[e[3],e[7]],2],'k',lw = 0.3,alpha=0.5)
            if labels == True:
                xa,ya,za = np.average(x[e,0]),np.average(x[e,1]),np.average(x[e,2])
                ax.text(xa,ya,za,'%i'%(ie),color='blue',fontsize=8.)
            ie += 1
        L = x.max()-x.min()
        ax.plot(np.average(x[:,0])+L/2,np.average(x[:,1])+L/2,np.average(x[:,2])+L/2,alpha=0.0)
        ax.plot(np.average(x[:,0])-L/2,np.average(x[:,1])-L/2,np.average(x[:,2])-L/2,alpha=0.0)
        

# Funciones para exportar resultados utilizando formato VTK
# cambiar el orden de la version de Matlab 
# o en formato h5 para luego utilziar gQuake especialmente par aproblemas no lineales