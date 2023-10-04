import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def lagrange(x,y):
    xSym = sp.symbols('x')
    n = len(x)
    pol = 0
    for i in range(0,n):
        fx = y[i]
        for j in range(0,n):
            if i != j:
                fx *= (xSym - x[j])/ (x[i]- x[j])
        pol += fx
    print(f'\nPolinomio obtenido por Lagrange sin simplificar: {pol}\n')
    return sp.simplify(pol)


def main():
    n = int(input("Ingrese el numero de iteraciones: "))
    x = []
    y = []
    for i in range(0,n):
        x.append(float(input(f'Ingrese su X{i}: ')))
    for i in range(0,n):
        y.append(float(input(f'Ingrese su f(X{i}): ')))
    
    pol = lagrange(x,y)
    print(f'Polinomio obtenido por lagrange simplificado: {pol}\n')

    xp = float(input("Ingrese un x para evaluar en la función: "))
    print(f'\nFunción obtenida por Lagrange evaluada en {xp}: {pol.subs("x",xp)}\n')

    grafica(pol,x,y,xp)

    return

def grafica(pol, x, y, z):
    xSym = 'x'
    graphX = np.linspace(y[0]-3,y[len(x)-1]-3,100)
    ecuacion_num = sp.lambdify(xSym, pol, 'numpy')
    graphY = ecuacion_num(graphX)
    
    plt.plot(graphX,graphY, label='Curva')

    for i in range (0,len(x)):
        plt.scatter(x[i],y[i],color='red',label=f'Punto({x[i]},{y[i]})')
    plt.scatter(z,pol.subs(xSym, z),color='yellow', label=f'P({z},{pol.subs(xSym, z)})')
    plt.grid(True)
    plt.axhline(y=0, color='gray', linestyle='--', label='y = 0')
    plt.legend()

    plt.show()
    
    return


if __name__ == "__main__":
    main()