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


if __name__ == "__main__":
    main()
