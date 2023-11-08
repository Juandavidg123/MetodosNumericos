import sympy as sp
import numpy as np
import matplotlib.pyplot as plt



def taylor(ecuacion, pasos, h, yci, xci, grado,rangoA):
    
    x = sp.symbols('x')
    y = sp.Function('y')(x)

    polinomioTaylor = ecuacion
    ecuacionDerivada = sp.diff(ecuacion, x)
    
    if (grado > 1):
        for i in range(2, grado + 1):
            polinomioTaylor = polinomioTaylor + ((ecuacionDerivada.subs(sp.Derivative(y, x), ecuacion) * h**(i-1))/sp.factorial(i))
            reemplazo = ecuacionDerivada.subs(sp.Derivative(y, x), ecuacion)
            ecuacionDerivada = sp.diff(reemplazo, x)
    
    yAprox = []
    yAprox.append(yci)
    for i in range(pasos):
        yNum = yci + h * polinomioTaylor.subs({x: rangoA +  i*h, y: yci})
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

def grafica(ecuacion, h, yAprox, yReal, rangoA):
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

    ecuacionInput = input("Ingrese la ecuacion en término de 'x' y 'y': ")
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

    grado = int(input("Ingrese el grado del polinomio de Taylor: "))

    yAprox = taylor(ecuacion, pasos, h, yCon, xCon, grado, rangoA)
    yReal = edo(ecuacionInput, xCon, yCon, pasos, h)

    for i in range(len(yAprox)):
        print(f"I: {i} Xi: {rangoA + i*h:.6f} yAprox: {yAprox[i]:.6f} Real: {yReal[0][i]:.6f} Er: {abs((yReal[0][i] - yAprox[i])/yReal[0][i]):.6f}")

    grafica(yReal[1], h, yAprox, yReal, rangoA)
    
    return


if __name__ == "__main__":
    main()