import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def solucion():
    print('''   Entrada de ecuaciones en términos de X y Y.
    El término de x se va a tomar como referencia para el despeje.
    Ejemplo: si se tiene f(x) = 5x - 4cos(x) = 0
    y se quiere despejar x = 4cos(x)/5,
    debes ingresar la función de la forma: 5*x - 4*cos(y)''')

    ecuacionInput = input("Ingrese su ecuación: ")
    ecuacion = sp.sympify(ecuacionInput)
    ecuacionXInput = ecuacionInput.replace('y','x')
    ecuacionX = sp.sympify(ecuacionXInput)
    
    x = sp.symbols('x')
    despeje = sp.solve(ecuacion, x)
    
    if criterio(despeje):
        puntoFijo(despeje, ecuacionX)
    else:
        print("No sirve este despeje de esta ecuación según el criterio de convergencia")

def puntoFijo(despeje, ecuacionX):
    x = float(input("Ingrese su x inicial: "))
    a = x
    tolerancia = float(input("Ingrese la tolerancia: "))
   
    i = 0
    er = 100000000
    while (er > tolerancia): 
        tempX = x
        x = despeje[0].subs('y', tempX) 
        xNum = x.evalf()
        er = abs((x - tempX) / x)  
        print(f"I: {i} x: {xNum}, er: {er.evalf()}")
        i += 1
        plt.scatter(x,despeje[0].subs('y',x),color='green')


    y = sp.symbols('y') 
    xSym = sp.symbols('x') 
    ecuacion_num = sp.lambdify(y, despeje[0].subs(xSym, x), 'numpy') 
    graphX = np.linspace(a - 3, a + 3, 100)
    graphY = ecuacion_num(graphX)
    
    ecuacionX_num = sp.lambdify(xSym, ecuacionX, 'numpy')
    graphY_ecuacionX = ecuacionX_num(graphX)
    plt.plot(graphX, graphY_ecuacionX, color='blue')

    plt.plot(graphX, graphY, color = 'violet')
    plt.ylim(min(graphY) - 3, max(graphY) + 3)
    plt.scatter(x, 0, color='red')
    plt.scatter(x, despeje[0].subs('y', x), color='yellow')
    plt.grid(True)
    plt.axhline(y=0, color='gray', linestyle='--', label='y = 0')
    plt.title("g(x): violeta; f(x): blue")
    plt.legend()
    plt.show()
    print("Solución evaluada en la función: ", ecuacionX.subs(xSym,x))
    return

def criterio(despeje):
    rango_input = input("Ingrese un x0 y x1 para el criterio de convergencia: ")
    numeros = rango_input.split()

    x0 = float(numeros[0])
    x1 = float(numeros[1])

    derivada = despeje[0].diff('y') 

    if abs(derivada.subs('y', x0)) < 1 and abs(derivada.subs('y', x1)) < 1:
        return True
    else:
        return False

def main():
    solucion()

if __name__ == "__main__":
    main()
