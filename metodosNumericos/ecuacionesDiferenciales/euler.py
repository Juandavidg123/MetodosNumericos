import sympy as sp

def solucion(ecuacion, rangoA, pasos, yci, h):
    x,y = sp.symbols('x y')
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
    ecuacionInput = ecuacionInput.replace('y', "y(x)")

    ecuacion = sp.sympify(ecuacionInput)
    ed = sp.Eq(y.diff(x), ecuacion)
    sol = sp.dsolve(ed)

    c = sp.solve(sol.subs({x: xci, y: yci}), c1)

    yReal = []

    for i in range(pasos + 1):
        yci = sol.rhs.subs({c1: c[0], x: xci})
        yReal.append(float(yci))
        xci = xci + h
    
    return yReal

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
        print(f"I: {i} Xi: {rangoA + i*h} yAprox: {yAprox[i]} yReal: {yReal[i]} Er: {abs((yReal[i] - yAprox[i])/yReal[i])}")


if __name__ == "__main__":
    main()