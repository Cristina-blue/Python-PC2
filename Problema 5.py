Suma_primos = 0

for num in range(2, 100):
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        Suma_primos += num

print(f"La suma de todos los números primos menores que 100 es: {Suma_primos}")
