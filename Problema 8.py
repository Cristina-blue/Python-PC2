def calcular_factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."

    elif n == 0:
        return 1
    
    else:
        return n * calcular_factorial(n - 1)
n = 9
resultado = calcular_factorial(n)
print(f"El factorial de {n} es: {resultado}")