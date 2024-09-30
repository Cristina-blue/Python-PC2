def es_numero_perfecto(n):
    #Suma de divisores propios de hasta n-1
    #No se toma en cuenta el mismo número, por eso es hasta n-1
    suma_divisores_de_n = sum(i for i in range(1, n) if n % i == 0)

    #Comprueba si la suma de divisores de n es igual al mismo n
    return suma_divisores_de_n == n

numeros_perfectos = [n for n in range(1, 1000) if es_numero_perfecto(n)]

print("Números perfectos menores que 1000:", numeros_perfectos)
