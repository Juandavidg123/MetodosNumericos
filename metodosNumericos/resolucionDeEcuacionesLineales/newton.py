import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def solucion():
    
    ecuacionInput = input("Ingrese su ecuacion en términos de x: ")
    ecuacion = sp.sympify(ecuacionInput)
    xSym = 'x'
    derivada = ecuacion.diff(xSym)
    
    x = float(input("Ingrese el valor de x inicial: "))
    a = x
    
    tolerancia = float(input("Ingrese el valor de la tolerancia: "))
    tempX = x
    
    if ecuacion.subs(xSym,x) == 0:
        return x
    er = 1000000000
    i = 0
    while (er > tolerancia):  
        tempX = x
        x = x - (ecuacion.subs(xSym,x)/derivada.subs(xSym,x))
        er = abs((x-tempX)/x)
        print(" I: ", "%03d" % i, " x: ", "%.6f" % x, " er: " + "%.6f" % er)
        i += 1
        plt.scatter(x,ecuacion.subs(xSym,x),color="green")
    
    graphX = np.linspace(a-3, a+3, 100)
    ecuacion_num = sp.lambdify(xSym, ecuacion, 'numpy')
    graphY = ecuacion_num(graphX)
    
    plt.plot(graphX, graphY)
    plt.ylim(min(graphY) - 3, max(graphY) + 3)
    plt.scatter(x,0,color='red')
    plt.grid(True)
    plt.axhline(y=0, color='gray', linestyle='--', label='y = 0')
    plt.legend()
    plt.show()
    print("Solución evaluada en la función: ", ecuacion.subs(xSym,x))
    return x

def main():
    print(f"Solución: {solucion()}")

if __name__ == "__main__":
    main()
