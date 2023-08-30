import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def solucion():
    ecuacionInput = input("Ingrese su ecuación en términos de x: ")
    ecuacion = sp.sympify(ecuacionInput)
    xSym = sp.Symbol('x')  # Usar la variable xSym en todo el código
    
    rango = input("Ingrese el x1 y x2: ")
    numeros = rango.split()

    x0 = float(numeros[0])
    x1 = float(numeros[1])
    a = x0


    tolerancia = float(input("Ingrese la tolerancia: "))
    er = 1000000
    i = 0
    while er > tolerancia:
        tempX1 = x1
        tempX0 = x0
        x1 = x0 - (ecuacion.subs(xSym, x0)) / ((ecuacion.subs(xSym, x1) - ecuacion.subs(xSym, x0)) / (x1 - x0))
        x0 = tempX1
        er = abs((x1 - x0) / x1)

        print(" I:", "%03d" % i, " Xn-1:", "%.6f" % tempX1, " f(Xn-1):", "%.6f" % ecuacion.subs(xSym, tempX1), " Xn-2:", "%.6f" % tempX0, " f(Xn-2):", "%.6f" % ecuacion.subs(xSym, tempX0), " Xn:", "%.6f" % x1, " er:", "%.6f" % er)
        i += 1
        plt.scatter(x1, ecuacion.subs(xSym, x1), color="green")

    graphX = np.linspace(a - 3, a + 3, 100)
    ecuacion_num = sp.lambdify(xSym, ecuacion, 'numpy')
    graphY = ecuacion_num(graphX)

    plt.plot(graphX, graphY)
    plt.ylim(min(graphY) - 3, max(graphY) + 3)
    plt.scatter(x1, 0, color='red')
    plt.grid(True)
    plt.axhline(y=0, color='gray', linestyle='--', label='y = 0')
    plt.show()
    return x1

def main():
    print(f"Solución: {solucion()}")

if __name__ == "__main__":
    main()
