import sympy as sp

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

    return


if __name__ == "__main__":
    main()