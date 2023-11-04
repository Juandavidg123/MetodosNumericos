import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def solucion(ecuacion, rangoA, pasos, yci, h):
    x = sp.symbols('x')
    y = sp.Function('y')(x)
    yAprox = [yci]
    for i in range(pasos):
        yNum = yci + h * ecuacion.subs({x: rangoA +  i*h, y: yci})
        yAprox.append(yNum)
        yci = yNum

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

def grafica(ecuacion, c, h, yAprox, yReal):
    xSym = sp.symbols('x')
    ySym = sp.Function('y')(xSym)

    xNum = h
    xVal = []

    for i in range(len(yAprox)):
        xVal.append(xNum)
        xNum += h

    xNum = h
    for i in range (len(yAprox)):
        plt.scatter(xNum,yAprox[i],color='red')
        xNum += h

    plt.plot(xVal, yReal[0], label='Solución Real', color='blue')
    plt.grid(True)
    plt.axhline(y=0, color='gray', linestyle='--', label='y = 0')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f"Gráfica de la ecuación solucionada: {ecuacion} con C = {c}")
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
        print(f"I: {i} Xi: {rangoA + i*h} yAprox: {yAprox[i]} Real: {yReal[0][i]} Er: {abs((yReal[0][i] - yAprox[i])/yReal[0][i])}")

    grafica(yReal[1], yReal[2], h, yAprox, yReal)

if __name__ == "__main__":
    main()