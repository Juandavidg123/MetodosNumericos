import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def diferenciasDivididas(x,y):
    n = len(x)
    difdiv = [y.copy()]
    for i in range (1,n):
        coeficientes = []
        for j in range(n-i):
            coeficiente = (difdiv[i-1][j+1] - difdiv[i-1][j])/(x[j+i]-x[j])
            coeficientes.append(coeficiente)
        difdiv.append(coeficientes)

    return difdiv

def polinomioProgresivo(difdiv, arr):
    x = sp.symbols('x')
    polinomio = difdiv[0][0]
    for i in range(1,len(difdiv)):
        a = difdiv[i][0]
        for j in range(i):
            a *= (x - arr[j])
        polinomio += a
    print(f"Polinomio progresivo sin simplificar: {polinomio}\n")
    return sp.simplify(polinomio)

def polinomioRegresivo(difdiv, arr):
    x = sp.symbols('x')
    polinomio = difdiv[0][-1]
    for i in range(1,len(difdiv)):
        a = difdiv[i][-1]
        for j in range(i):
            a *= (x - arr[len(difdiv)-1-j])
        polinomio += a
    print(f"Polinomio regresivo sin simplificar: {polinomio}\n")
    return sp.simplify(polinomio)

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

def main():
    n = int(input("Ingrese el numero de iteraciones: "))
    x = []
    y = []
    for i in range(0,n):
        x.append(float(input(f'Ingrese su X{i}: ')))
    for i in range(0,n):
        y.append(float(input(f'Ingrese su f(X{i}): ')))
      
    coeficientes = diferenciasDivididas(x, y)
    
    ite = []
    for i in range(0,len(x)):
        ite.append(i)

    print(f'i: {ite}')
    print(f'Xi: {x}')
    
    for i, coef in enumerate(coeficientes):
        print(f'Diferencia dividida de orden {i+1}: {coef}')

    print("\n")
    polpro = polinomioProgresivo(coeficientes, x)
    print(f"Polinomio progresivo: {polpro}\n")

    polreg = polinomioRegresivo(coeficientes, x)
    print(f"Polinomio regresivo: {polreg}\n")

    xpp = float(input("Ingrese un número x para evaluarlo en la función progresiva: "))

    xpr = float(input("\nIngrese un número x para evaluarlo en la función regresiva: "))


    print(f'\nPolinomio progresivo evaluado con un x = {xpp}: {polpro.subs("x",xpp)}\n')
    print(f'Polinomio regresivo evaluado con un x = {xpr}: {polpro.subs("x",xpr)}\n')

    grafica(polpro,x,y,xpp)

if __name__ == "__main__":
    main()
