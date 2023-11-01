import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def solucion():
    
    ecuacionInput = input("Ingrese su ecuacion en términos de x: ")
    ecuacion = sp.sympify(ecuacionInput)
    xSym = 'x'
    
    rango = input("Ingrese el rango de menor a mayor: ")
    numeros = rango.split()

    a = float(numeros[0])
    b = float(numeros[1])
    ag = a


    x = (a + b) / 2
    noSolution = "No hay solución"
    if ecuacion.subs(xSym,a) == 0:
        return a
    elif ecuacion.subs(xSym,b) == 0:
        return b
    elif (ecuacion.subs(xSym,a) > 0 and ecuacion.subs(xSym,b) > 0) or (ecuacion.subs(xSym,a) < 0 and ecuacion.subs(xSym,b) < 0):
        return noSolution
    else:
        i = 0
        er = 100
        tolerancia = float(input("Ingrese el valor de tolerancia: "))
        while (er > tolerancia):
            tempA = a
            tempB = b
            tempX = x

            if ecuacion.subs(xSym,a) * ecuacion.subs(xSym,x) > 0:
                a = x
                x = (x + b) / 2
            else:
                b = x
                x = (x + a) / 2

            if i == 0:
                er = 1000000000000
            else:
                er = abs((x - tempX) / x)
            i = i + 1
            print(" I: ", "%03d" % i, " a: ", "%.6f" % tempA, " b: ", "%.6f" % tempB, " p: ",
                  "%.6f" % tempX, " f(a): ", "%.6f" % ecuacion.subs(xSym,tempA), " f(p): ", "%.6f" % ecuacion.subs(xSym,tempX),
                  " er: " + "%.6f" % er)
            plt.scatter(x,ecuacion.subs(xSym,x),color='green')

        graphX = np.linspace(ag-3,ag+3,100)
        ecuacion_num = sp.lambdify(xSym, ecuacion, 'numpy')
        graphY = ecuacion_num(graphX)
        
        plt.plot(graphX,graphY)
        plt.ylim(min(graphY) - 3, max(graphY) + 3)
        plt.scatter(x,0,color='red')
        plt.grid(True)
        plt.axhline(y=0, color='gray', linestyle='--', label='y = 0')
        plt.legend()
        plt.show()
        print("Solución evaluada en la función: ", ecuacion.subs(xSym,x))
        return x

def main():
    print(f"Solucion: {solucion()}")

if __name__ == "__main__":
    main()
