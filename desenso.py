from matplotlib import cm
import numpy as np 
import matplotlib.pyplot as plt


def f(x,y):
    return x**2 + y**2 

def derivate(cp, p ,h):
    return (f(cp[0], cp[1]) - f(p[0], p[1]))/h

def gradiente(p, h):
    grad = np.zeros(2)
    for idx, _ in enumerate(p):
        cp = np.copy(p)
        cp[idx] = cp[idx] + h

        dp = derivate(cp, p, h)
        grad[idx] = dp

    return grad

if __name__=='__main__':

    fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
    
    res = 100

    x = np.linspace(-4, 4, res)
    y = np.linspace(-4, 4, res)
    X, Y = np.meshgrid(x,y)

    Z = f(X,Y)

    surf = ax.plot_surface(X, Y, Z,cmap=cm.cool)
    fig.colorbar(surf)
    plt.show()

    fig, ax = plt.subplots(1,1)
    level_map =np.linspace(np.min(Z), np.max(Z), res)
    plt.contourf(X,Y,Z,level_map, cmap=cm.cool)
    plt.colorbar()
    plt.title("Descenso del gradiente")
    #plt.show()

    p = np.random.rand(2) * 8 - 4
    plt.plot(p[0], p[1], 'o', c='k')

    h = 0.01
    lr = 0.01

    for i in range(10000):
        p = p - lr * gradiente(p,h)
        if(i % 10 == 0):
            plt.plot(p[0], p[1], 'o', c='r')
            
    plt.plot(p[0], p[1], 'o', c='w')        
    plt.show()