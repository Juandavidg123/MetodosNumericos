import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def solucion(ecuacion, rangoA, pasos, yci, h):
    x = sp.symbols('x')
    y = sp.Function('y')(x)
    yAprox = [yci]
    for i in range(pasos):
        k1 = h * ecuacion.subs({x: rangoA, y: yci})
        k2 = h * ecuacion.subs({x: rangoA + h/2, y: yci + k1/2})
        k3 = h * ecuacion.subs({x: rangoA + h/2, y: yci + k2/2})
        k4 = h * ecuacion.subs({x: rangoA + h, y: yci + k3})
        yNum = yci + (k1 + 2*k2 + 2*k3 + k4)/6
        yAprox.append(yNum)
        yci = yNum
        rangoA = rangoA + h

    return yAprox

def edo(ecuacionInput, xci, yci, pasos, h):

    x = sp.symbols('x')
    y = sp.Function('y')(x)
    c1 = sp.symbols("C1")

    ecuacion = sp.sympify(ecuacionInput)
    ed = sp.Eq(y.diff(x), ecuacion)
    sol = sp.dsolve(ed)

    c = sp.solve(sol.subs({x: xci, y: yci}), c1)
    print(f"C: {c}")
    print(f"Ecuación: {sol}")

    yReal = []

    for i in range(pasos + 1):
        yci = sol.rhs.subs({c1: c[0], x: xci})
        yReal.append(yci)
        xci = xci + h

    return [yReal, sol, c[0]]

def grafica(h, yAprox, yReal, rangoA):
    xSym = sp.symbols('x')
    c1 = sp.symbols("C1")

    pasos = rangoA
    
    for i in range (len(yAprox)):
        plt.scatter(pasos,yAprox[i],color='red')
        pasos += h

    yGraph = sp.lambdify(xSym, yReal[1].rhs.subs({c1: yReal[2]}), "numpy")
    xNum = np.linspace(rangoA, pasos, 100)
    yEcuacion = yGraph(xNum)

    plt.plot(xNum, yEcuacion, color='blue', label='Solución exacta')
    plt.grid(True)
    plt.axhline(y=0, color='gray', linestyle='--', label='y = 0')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def main():
    ecuacionInput = input("Ingrese su ecuacion en términos de 'x' y 'y': ")
    ecuacion = sp.sympify(ecuacionInput)

    rangos = input("Ingrese el rango de valores de menor a mayor: ")
    rangos = rangos.split(" ")
    rangoA = float(rangos[0])
    rangoB = float(rangos[1])

    pasos = int(input("Ingrese la cantidad de pasos que desea: "))
    h = (rangoB - rangoA)/pasos

    condicionInicial = input("Ingrese la condicion inicial y(x0) = y0, primero x0 y luego y0: ")
    condicionInicial = condicionInicial.split(" ")
    xCon = float(condicionInicial[0])
    yCon = float(condicionInicial[1])

    yAprox = solucion(ecuacion, rangoA, pasos, yCon, h)
    yReal = edo(ecuacionInput, xCon, yCon, pasos, h)

    for i in range(len(yAprox)):
        print(f"I: {i} Xi: {rangoA + i*h:.6f} yAprox: {yAprox[i]:.6f} Real: {yReal[0][i]:.6f} Er: {abs((yReal[0][i] - yAprox[i])/yReal[0][i]):.6f}")

    grafica(h, yAprox, yReal, rangoA)

if __name__ == "__main__":
    main()